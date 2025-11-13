import sqlite3
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import re
from datetime import datetime

DB_PATH = "oca_courses.db"
LOG_FILE = "scrape_log.txt"

def log_message(message):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {message}\n")

def scrape_text(url):
    try:
        response = requests.get(url, timeout=10)
        response.encoding = response.apparent_encoding
        soup = BeautifulSoup(response.text, "html.parser")

        # --- タイトル ---
        title = soup.title.string.strip() if soup.title else "No Title"

        # --- 主要本文抽出 ---
        # まず、コース詳細部分（div.courseDetailなど）を優先的に抽出
        main_section = (
            soup.find("div", class_="courseDetail")
            or soup.find("section", class_="course-detail")
            or soup.find("main")
            or soup.body
        )

        texts = []
        for tag in main_section.find_all(["h1", "h2", "h3", "p", "li"]):
            text = tag.get_text(" ", strip=True)
            if len(text) > 10 and not any(x in text for x in [
                "OCA大阪デザイン＆テクノロジー専門学校",
                "大阪テック",
                "学校紹介",
                "交通アクセス",
                "情報公開",
                "文部科学大臣認定",
                "職業実践専門課程",
                "©",
                "All rights reserved"
            ]):
                texts.append(text)

        # --- テキスト整形 ---
        content = "\n".join(texts)
        content = re.sub(r"\s+", " ", content)  # 余分な改行や空白を除去
        content = re.sub(r"(大阪テック｜)?OCA⼤阪デザイン&テクノロジー専⾨学校.*?業界のプロになる", "", content)
        content = re.sub(r"(OCA|大阪テック).*?(デザイン|テクノロジー)", "", content)
        content = content.strip()

        # --- 内容が短すぎる場合は本文全体から抽出 ---
        if len(content) < 100:
            fallback_texts = [t.get_text(" ", strip=True) for t in soup.find_all("p") if len(t.get_text(strip=True)) > 20]
            content = "\n".join(fallback_texts)

        return title, content

    except Exception as e:
        print(f"⚠️ 取得失敗: {url} ({e})")
        return None, None



def build_database():
    """全コースページをスクレイピングしてDB作成（FTS対応）"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # 通常テーブル
    c.execute("CREATE TABLE IF NOT EXISTS courses (url TEXT PRIMARY KEY, title TEXT, content TEXT)")
    # FTSテーブル（全文検索用）
    c.execute("CREATE VIRTUAL TABLE IF NOT EXISTS courses_fts USING fts5(title, content, url, content='courses', content_rowid='rowid')")

    conn.commit()

    base_url = "https://www.oca.ac.jp/course/"
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, "html.parser")

    links = [a["href"] for a in soup.find_all("a", href=True) if "/course/" in a["href"]]
    links = list(set([l if l.startswith("http") else f"https://www.oca.ac.jp{l}" for l in links]))

    print(f"🌐 取得対象: {len(links)}件")
    log_message(f"=== スクレイピング開始（{len(links)}件） ===")

    failed = []

    for url in tqdm(links):
        title, content = scrape_text(url)
        if content and len(content.strip()) > 50:
            c.execute("INSERT OR REPLACE INTO courses VALUES (?, ?, ?)", (url, title, content))
        else:
            failed.append(url)

    # FTSインデックス再構築
    c.execute("INSERT INTO courses_fts(courses_fts) VALUES ('rebuild')")
    conn.commit()
    conn.close()
    print("💾 データベース作成完了！")

    if failed:
        print(f"⚠️ 本文が取得できなかったURL: {len(failed)}件")
        for f in failed[:5]:
            print(" -", f)
        log_message(f"本文なしURL: {len(failed)}件")


def search_courses(query):
    """FTSで全文検索"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT title, content, url FROM courses_fts WHERE courses_fts MATCH ?", (query,))
    results = c.fetchall()
    conn.close()
    return results


def main():
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.execute("SELECT 1 FROM courses LIMIT 1")
        conn.close()
    except:
        print("⚙️ DBがありません。スクレイピングを実行しますか？(y/n): ", end="")
        if input().lower() == "y":
            build_database()
        else:
            print("終了します。")
            return

    while True:
        query = input("\n💬 質問を入力してください（終了: exit）\n> ")
        if query.lower() == "exit":
            break
        results = search_courses(query)
        if results:
            print(f"\n🔎 {len(results)}件ヒットしました：")
            for title, content, url in results[:3]:
                snippet = re.sub(r"\s+", " ", content[:200])
                print(f"\n📘 {title}\n🧾 {snippet}...\n🌐 {url}")
        else:
            print("該当データが見つかりませんでした。")


if __name__ == "__main__":
    main()