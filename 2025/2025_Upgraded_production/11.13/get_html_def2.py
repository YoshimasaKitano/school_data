import requests
from bs4 import BeautifulSoup
import json
import os

def scrape_from_heading(url, output_filename="scraped.json"):
    response = requests.get(url)
    response.encoding = response.apparent_encoding
    soup = BeautifulSoup(response.text, "html.parser")

    # 抽出対象タグ（優先順）
    tags_to_extract = ["h1", "h2", "h3", "h4", "h5", "h6", "p", "ul", "li"]
    block_words = []

    # mainタグを本文領域として取得
    main = soup.find("main")
    if not main:
        print("mainタグが見つかりませんでした。本文を特定できません。")
        return

    # main内で、最初に出てくる対象タグを探す（開始地点）
    start_elem = None
    for tag in tags_to_extract:
        start_elem = main.find(tag)
        if start_elem:
            break

    if not start_elem:
        print("mainタグ内に対象タグ（h1〜li）が見つかりませんでした。")
        return

    # main内の全対象タグを取得
    elements = main.find_all(tags_to_extract)

    # 開始地点以降のみ抽出
    start_index = elements.index(start_elem)
    target_elements = elements[start_index:]

    # テキスト抽出
    for elem in target_elements:
        text = elem.get_text(strip=True)
        if text:
            block_words.append({
                "tag": elem.name,
                "text": text
            })

    # 重複削除
    unique_blocks = []
    seen = set()
    for block in block_words:
        key = (block["tag"], block["text"])
        if key not in seen:
            unique_blocks.append(block)
            seen.add(key)
    block_words = unique_blocks

    # dataフォルダ準備
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(base_dir, "data")
    os.makedirs(data_dir, exist_ok=True)

    json_path = os.path.join(data_dir, output_filename)

    # JSON保存
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(block_words, f, ensure_ascii=False, indent=2)

    print(f"{len(block_words)} 件のデータを保存しました。")

# 使用例
url = "https://www.oca.ac.jp/media_info/"
scrape_from_heading(url)

