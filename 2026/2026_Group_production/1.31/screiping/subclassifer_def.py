import json
import os
import re

"""
このファイルはJSONファイルを読み込み、ページカテゴリを推定し、結果を出力しつつ辞書型で返す関数とそれをテストするためのコードが書かれています。
"""

def subclassify():
    # パスの準備
    ## このファイルのディレクトリ階層を変数へ代入する
    base_dir = os.path.dirname(os.path.abspath(__file__))

    ## 読み込むjsonファイルのバスを変数に代入する
    json_path = os.path.join(base_dir, "data", "scraped.json")

    # カテゴリ分けをする準備
    ## 保存する形式を設定
    result = {
        "used_text": None,
        "subcategory": None,
        "error": None,
    }

    # JSON読み込み
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            scraped_data = json.load(f)

            ## list型かどうかの確認（もし違うならエラーを出力）
            if not isinstance(scraped_data, list):
                raise ValueError("JSONはリスト形式である必要があります。")

    except Exception as e:
        ## エラーならエラーの項目にエラーを代入する
        result["error"] = f"JSON読み込みエラー: {e}"
        return result

    # h1 → h2 → h3 → p の順でテキスト抽出する
    def extract_texts(tag, limit=None):

        ## タグとテキストが入るリストを作る
        texts = []

        for item in scraped_data:
            ## tagが一致しているか
            if item.get("tag") != tag:
                continue
            
            ## テキストをリストに入れる準備をする
            text = item.get("text")
            if not text:
                continue
            
            ## 空白処理をしてリストに入れる
            texts.append(text.strip())

            ## 件数制限があれば超えたら終了
            if limit is not None and len(texts) >= limit:
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

    # サブカテゴリ分類
    ## サブカテゴリ分けで使うtextを入れる変数を作成する
    subcategory = None

    ## [○○専攻]という文字列を探して○○の部分を抜き出す処理
    match = re.search(r"([^\s　]+)専攻", used_text)

    if match:
        name = match.group(1)
        ## 「専攻情報」など「専攻」単体扱いのものは除外する
        if name != "" and name != "専攻" and not name.endswith("情報"):
            subcategory = f"{name}専攻"

    ## 最終保存先に入力する
    result["subcategory"] = subcategory

    return result

# result = subclassify()
# print(result)