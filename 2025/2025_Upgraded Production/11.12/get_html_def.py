import requests
from bs4 import BeautifulSoup
import json
import os

def scrape_from_heading(url, output_filename="scraped.json"):
    response = requests.get(url)
    response.encoding = response.apparent_encoding
    soup = BeautifulSoup(response.text, "html.parser")

    tags_to_extract = ["h1", "h2", "h3", "h4", "h5", "h6", "p", "ul", "li"]
    block_words = []

    # h1 → h2 の優先順で開始タグを探す
    start_elem = soup.find("h1") or soup.find("h2")
    if not start_elem:
        print("h1 または h2 が見つかりませんでした。")
        return

    # 抽出開始
    elements = []
    for elem in start_elem.find_all_next(tags_to_extract + ["footer"]):
        if elem.name == "footer":
            break
        elements.append(elem)

    # 開始タグもリストに含める
    elements.insert(0, start_elem)

    # テキスト抽出
    for elem in elements:
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

    # dataフォルダの準備
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(base_dir, "data")
    os.makedirs(data_dir, exist_ok=True)

    json_path = os.path.join(data_dir, output_filename)

    # JSONとして保存
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(block_words, f, ensure_ascii=False, indent=2)

    print(f"{len(block_words)} 件のデータを保存しました。")
    print(f"保存先: {json_path}")

# 使用例
# url = "https://www.oca.ac.jp/course/technology/white-hacker/"
# scrape_from_heading(url)
