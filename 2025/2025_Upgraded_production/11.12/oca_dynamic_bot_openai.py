import sqlite3
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import re
from datetime import datetime
from openai import OpenAI
import time  # ← これを追加！

DB_PATH = "oca_courses.db"
LOG_FILE = "scrape_log.txt"
client = OpenAI()  # ← OpenAIクライアント

def log_message(message):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {message}\n")


# --- (既存の scrape_text, build_database は変更不要) ---


def search_courses(query):
    """FTSで全文検索"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT title, content, url FROM courses_fts WHERE courses_fts MATCH ?", (query,))
    results = c.fetchall()
    conn.close()
    return results


# --------------------------
# 💬 ChatGPTによる動的要約
# --------------------------
def summarize_text(text):
    try:
        # 要約対象が長すぎるとトークンコストが増えるので冒頭1000字程度に制限
        text = text[:1000]
        prompt = f"以下の文章を、専門学校のコース説明として200文字以内で分かりやすく要約してください。\n{text}"

        res = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300,
            temperature=0.5
        )

        time.sleep(3)  # ← ここでAPI負荷を下げるため3秒待つ！

        return res.choices[0].message.content.strip()

    except Exception as e:
        print(f"⚠️ 要約失敗: {e}")
        time.sleep(3)  # ← 失敗時も少し待機
        return None


def main():
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.execute("SELECT 1 FROM courses LIMIT 1")
        conn.close()
    except:
        print("⚙️ DBがありません。スクレイピングを実行しますか？(y/n): ", end="")
        if input().lower() == "y":
            from oca_dynamic_bot import build_database
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
                print(f"\n📘 {title}")
                summary = summarize_text(content)
                if summary:
                    print(f"🧾 要約: {summary}")
                else:
                    snippet = re.sub(r"\s+", " ", content[:200])
                    print(f"🧾 {snippet}...")
                print(f"🌐 {url}")
        else:
            print("該当データが見つかりませんでした。")


if __name__ == "__main__":
    main()