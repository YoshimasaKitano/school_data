import json
from transformers import pipeline

# 分類モデル準備
model_name = "taishi-i/awesome-japanese-nlp-classification-model"
classifier = pipeline("text-classification", model=model_name)

# 任意のマッピングルール
def map_to_four_categories(text):
    text_lower = text.lower()
    if "専攻" in text or "ホワイトハッカー" in text:
        return "専攻情報"
    elif "学園祭" in text or "イベント" in text or "発表会" in text:
        return "イベント情報"
    elif "お知らせ" in text or "news" in text:
        return "お知らせ"
    else:
        return "学校概要"

def classify_page_by_heading(json_path):
    """scraped.json の h1/h2 を使ってページ全体のカテゴリを判定"""
    with open(json_path, "r", encoding="utf-8") as f:
        scraped_data = json.load(f)

    # h1優先
    h1_texts = [item["text"] for item in scraped_data if item.get("tag") == "h1"]
    if h1_texts:
        target_text = h1_texts[0]
    else:
        # h1がなければh2上位3つ
        h2_texts = [item["text"] for item in scraped_data if item.get("tag") == "h2"][:3]
        target_text = " ".join(h2_texts)

    # モデル分類結果は無視して、強制マッピング
    category = map_to_four_categories(target_text)

    print("=== 分類結果 ===")
    print(f"カテゴリ: {category}")
    print(f"使用テキスト: {target_text}")

    return category

# 実行例
category = classify_page_by_heading("data/scraped.json")



