import json
import os
from transformers import pipeline

"""
このファイルはJSONファイルを読み込み、ページカテゴリを推定し、結果を出力しつつ辞書型で返す関数とそれをテストするためのコードが書かれています。
カテゴリ分けには手動と自動を切り替えることができ、手動ならキーワードに一致すれば、自動ならタイトルをみて、自動でカテゴリ分けをします。

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

def classify(use_model: bool = False):

    # data/scraped.jsonを参照する
    ## このファイルが入っているディレクトリパスを変数に代入
    base_dir = os.path.dirname(os.path.abspath(__file__))

    ## ディレクトリの中にあるjsonファイルを見つけてファイルパスを変数に代入
    json_path = os.path.join(base_dir, "data", "scraped.json")

    # カテゴリ分けをする準備
    ## 保存する形式を設定
    result = {
        "category": None,
        "used_text": None,
        "model_result": None,
        "error": None
    }

    try:
        ## JSON読み込み
        with open(json_path, "r", encoding="utf-8") as f:
            scraped_data = json.load(f)

            ## list型かどうかの確認（もし違うならエラーを出力）
            if not isinstance(scraped_data, list):
                raise ValueError("JSONはリスト形式である必要があります。")
                
    except Exception as e:
        ## エラーならエラーの項目にエラーを代入する
        result["error"] = f"JSON読み込みエラー: {e}"
        return result

    # テキスト抽出
    ## 指定したタグのテキストだけを抜き出す関数
    def extract_texts(tag, limit=None):

        ## タグとテキストが入るリストを作る
        texts = []

        for item in scraped_data:
            ## tagが一致してるか
            if item.get("tag") != tag:
                continue
            
            ## テキストをリストに入れる準備をする
            text = item.get("text")
            if not text:
                continue
            
            ## 空白処理をしてリストに入れる
            texts.append(text.strip())

            ## 件数制限があれば超えたら終了
            if limit and len(texts) >= limit:
                break

        return texts

    # 優先順位で見出しテキストを取得
    ## カテゴリ分けで使うtextを入れる変数を作成する
    used_text = ""

    ## 優先順で使うtextを探す　なければエラーを変数に代入する
    for tag, limit in [("h1", None), ("h2", 3), ("h3", 3), ("p", 3)]:

        ## タグとtextを取得
        texts = extract_texts(tag, limit)

        ## ひとつもとれていなければ処理をとばす
        if texts:
            used_text = " ".join(texts)
            break
    
    ## ひとつもとれていなければエラーを出力する
    if not used_text:
        result["error"] = "有効な見出しテキストが見つかりませんでした。"
        return result

    ## 最終保存先に入力する
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

    ## 最終保存先に入力する
    if use_model == False:
        result["category"] = map_to_four_categories(used_text)

    # AI推論
    if use_model:
        try:
            ## モデルなどの指定
            classifier = pipeline("text-classification", model="taishi-i/awesome-japanese-nlp-classification-model")

            ## クラス分けをするAIの設定
            model_output = classifier(used_text[:1024])

            ## 判別スコアの代入
            result["model_result"] = model_output
            
            ## 判別のラベルを指定
            LABEL_MAP = {
                "0": "学校概要",
                "1": "専攻情報",
                "2": "イベント情報",
                "3": "お知らせ",
            }

            ## 最終保存先に入力する
            label = model_output[0]["label"]
            result["category"] = LABEL_MAP.get(label, "不明")

        ## エラーが出た際はエラーを最終保存先に入力する
        except Exception as e:
            result["error"] = f"モデル読み込み/推論エラー: {e}"

    return result


# # 実行例：
# if __name__ == "__main__":
#     res = classify(use_model=True)
#     print(res)
