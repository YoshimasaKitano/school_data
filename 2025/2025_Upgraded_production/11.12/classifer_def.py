def classify(use_model: bool = False):
    """
    JSONファイルを読み込み、ページカテゴリを推定し、
    結果を出力しつつ辞書型で返す関数。

    Args:
        use_model (bool): Trueの場合、transformersモデルでの推論を実行する

    Returns:
        dict: {
            "category": <判定カテゴリ>,
            "used_text": <カテゴリ判定に使用したテキスト>,
            "model_result": <transformersモデルの分類結果 or None>,
            "error": <エラーが発生した場合のメッセージ or None>
        }
    """

    import json
    import os

    # スクリプトのあるフォルダからdata/scraped.jsonを参照
    base_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(base_dir, "data", "scraped.json")

    result = {
        "category": None,
        "used_text": None,
        "model_result": None,
        "error": None
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

    # テキスト抽出
    def extract_texts(tag, limit=None):
        texts = [
            item.get("text", "").strip()
            for item in scraped_data
            if item.get("tag") == tag and item.get("text")
        ]
        return texts[:limit] if limit else texts

    # 優先順位で見出しテキストを取得
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

    # カテゴリ分類（ルールベース）
    def map_to_four_categories(text):
        if "専攻" in text:
            return "専攻情報"
        if "学園祭" in text or "イベント" in text or "制作展" in text:
            return "イベント情報"
        if "お知らせ" in text or "news" in text.lower():
            return "お知らせ"
        return "学校概要"

    result["category"] = map_to_four_categories(used_text)

    print(f"カテゴリ: {result['category']}")
    print(f"判定に使用したテキスト: {used_text}")

    # モデル推論（任意）
    if use_model:
        try:
            from transformers import pipeline
            classifier = pipeline("text-classification", model="taishi-i/awesome-japanese-nlp-classification-model")
            model_output = classifier(used_text[:1024])
            result["model_result"] = model_output
            print(f"モデル出力: {model_output}")
        except Exception as e:
            result["error"] = f"モデル読み込み/推論エラー: {e}"
            print(f"⚠️ {result['error']}")

    print("=== 分類終了 ===\n")
    return result


# # 実行例：
# if __name__ == "__main__":
#     res = classify(use_model=False)
#     print(res)
