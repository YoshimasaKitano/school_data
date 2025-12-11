import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def get_url(base_url):

    domain = urlparse(base_url).netloc

    visited_list = []  # 訪問済みURLを順番に保存するリスト
    to_visit = [base_url]

    # 除外する拡張子（画像・ファイル類）
    exclude_ext = (".jpg", ".jpeg", ".png", ".gif", ".pdf", ".css", ".js", ".zip", ".ico", ".svg", ".mp4", ".mov")

    # 除外するURLパターン
    exclude_keywords = ("blog", "glossary", "corona", "system", "feature", "#", "abroad-")

    while to_visit:
        url = to_visit.pop(0)

        if url in visited_list:
            continue

        visited_list.append(url)
        print(f"取得中: {url}")

        try:
            response = requests.get(url, timeout=10)
        except requests.RequestException as e:
            print(f"リクエスト失敗: {url} ({e})")
            continue

        soup = BeautifulSoup(response.text, "html.parser")

        # ここで本文抽出・分類などに渡す
        # analyze_page(soup)

        for a in soup.find_all("a", href=True):
            link = urljoin(url, a["href"])
            link_domain = urlparse(link).netloc

            # 除外条件
            if not link.startswith("https://"):
                continue
            if link_domain != domain:
                continue
            if link.endswith(exclude_ext):
                continue
            if any(keyword in link for keyword in exclude_keywords):
                continue
            if link in visited_list or link in to_visit:
                continue

            to_visit.append(link)

    print("全ての内部リンク取得完了！")
    return visited_list  # 訪問順にURLリストを返す

# 実行例
# urls = get_url("https://www.oca.ac.jp/")
# print(urls)
