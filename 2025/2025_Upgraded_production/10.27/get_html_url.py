"""
pip install requests
pip install beautifulsoup4
pip install openAI
"""

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

base_url = "https://www.oca.ac.jp/"
domain = urlparse(base_url).netloc

visited_urls = set()
to_visit = [base_url]

# 除外する拡張子（画像・ファイル類）
exclude_ext = (".jpg", ".jpeg", ".png", ".gif", ".pdf", ".css", ".js", ".zip", ".ico", ".svg", ".mp4", ".mov")

# 除外するURLパターン
exclude_keywords = ("blog", "glossary","corona","system","feature","#","abroad-")

while to_visit:
    url = to_visit.pop(0)
    if url in visited_urls:
        continue

    visited_urls.add(url)
    print(f"▶ 取得中: {url}")

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # ここで本文抽出・分類などに渡す
    # analyze_page(soup)

    for a in soup.find_all("a", href=True):
        link = urljoin(url, a["href"])
        link_domain = urlparse(link).netloc

        # 除外条件
        if not link.startswith("https://"):
            continue
        if not domain == link_domain:
            continue
        if link.endswith(exclude_ext):
            continue
        if any(keyword in link for keyword in exclude_keywords):
            continue
        if link in visited_urls:
            continue

        to_visit.append(link)

print("✅ 全ての内部リンク取得完了！")



