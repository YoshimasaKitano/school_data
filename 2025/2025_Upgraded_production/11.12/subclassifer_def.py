import json
import os
import re

def subclassify():
    # スクリプトと同じ階層の data/scraped.json を参照
    base_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(base_dir, "data", "scraped.json")

    result = {
        "used_text": None,
        "subcategory": None,  # サブカテゴリ用
        "error": None,
    }

    print(f"\n=== {json_path} の分類開始 ===")

    # JSON読み込み
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            scraped_data = json.load(f)
            if not isinstance(scraped_data, list):
                raise ValueError("JSONはリスト形式である必要があります。")
    except Exception as e:
        result["error"] = f"JSON読み込みエラー: {e}"
        print(f"❌ {result['error']}")
        return result

    # h1 → h2 → h3 → p の順でテキスト抽出
    def extract_texts(tag, limit=None):
        texts = [
            item.get("text", "").strip()
            for item in scraped_data
            if item.get("tag") == tag and item.get("text")
        ]
        return texts[:limit] if limit else texts

    used_text = ""
    for tag, limit in [("h1", None), ("h2", 3), ("h3", 3), ("p", 3)]:
        texts = extract_texts(tag, limit)
        if texts:
            used_text = " ".join(texts)
            break

    if not used_text:
        result["error"] = "有効な見出しテキストが見つかりませんでした。"
        print(f"⚠️ {result['error']}")
        return result

    result["used_text"] = used_text
    print(f"判定に使用したテキスト: {used_text}")

    # === サブカテゴリー判定 ===
    subcategory = None
    match = re.search(r"([^\s　]+)専攻", used_text)
    if match:
        name = match.group(1)
        # 「専攻情報」など「専攻」単体扱いのものは除外
        if name != "" and name != "専攻" and not name.endswith("情報"):
            subcategory = f"{name}専攻"

    result["subcategory"] = subcategory
    print(f"サブカテゴリー: {subcategory if subcategory else 'None'}")

    return result

# result = subclassify()
# print(result)