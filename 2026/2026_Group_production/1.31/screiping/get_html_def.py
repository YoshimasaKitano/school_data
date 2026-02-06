import requests
from bs4 import BeautifulSoup
import json
import os

"""
このファイルは[指定したURLの中のをすべてとってくる関数]とそのテストをおこなうことができるコードのみを書いているファイルです。
引数でURLとファイル名をを入力し、そのURLの中に書いているHTMLのタグとtextをこのファイルと同じディレクトリ階層にフォルダを作り、その中に引数の中のファイル名でファイルを作成し、データを保存します。
"""

def scrape_from_heading(url, output_filename="scraped.json"):
    
    # スクレイピングをするために予期せぬ動きにならないようにあらかじめ、設定をする
    ## HTMLの内容をとってくる
    response = requests.get(url)

    ## 文字コードを強制的に使わせてる
    response.encoding = response.apparent_encoding 

    ## 取得したHTMLを解析して、タグとかを扱いやすくする
    soup = BeautifulSoup(response.text, "html.parser") 

    ## どのタグを取ってくるのかを指定
    tags_to_extract = ["h1", "h2", "h3", "h4", "h5", "h6", "p", "ul", "li"] 

    ## HTMLのタグとtextを入れるリストを準備する
    block_words = [] 

    # スクレイピングを始める場所を h1 → h2 とし、優先順で開始タグを探す
    start_elem = soup.find("h1") or soup.find("h2")
    if not start_elem:
        print(f"{url}でh1 または h2 が見つかりませんでした。")
        return

    # 抽出開始
    ## とってきたタグを保存するリスト
    elements = []

    ## すべてのタグを保存し、footerのタグが出れば処理を終了する
    for elem in start_elem.find_all_next(tags_to_extract + ["footer"]):
        if elem.name == "footer":
            break
        elements.append(elem)

    ## find_all_nextを使っているため、開始タグもリストに含める
    elements.insert(0, start_elem)

    # テキスト抽出
    ## タグの中のtextをタグとtextに分けて保存する。
    for elem in elements:
        text = elem.get_text(strip=True)
        ## textがないものは処理を飛ばす。
        if text:
            block_words.append({
                "tag": elem.name,
                "text": text
            })

    # 重複削除
    ## 重複していないタグとtextと入れるリストを作成
    unique_blocks = []

    ## 重複したものが入らないデータ型にする
    seen = set()

    ## 1つ1つリストの要素を別のリストに入れるが、そのリストに同じものが入っているならリストに入れない処理
    for block in block_words:
        key = (block["tag"], block["text"])
        if key not in seen:
            unique_blocks.append(block)
            seen.add(key)

    ## 一度違う変数に入れ替える。(別で作ったため、変数名が合わなかったため)
    block_words = unique_blocks

    # dataフォルダの準備
    ## このPythonファイル自身が入っているディレクトリを変数に代入
    base_dir = os.path.dirname(os.path.abspath(__file__)) 

    ## 同じ階層に data フォルダを指定
    data_dir = os.path.join(base_dir, "data")

    ## data フォルダを作る(エラーを出さない)
    os.makedirs(data_dir, exist_ok=True)

    ## 最終保存先を変数に指定
    json_path = os.path.join(data_dir, output_filename)

    # JSONとして保存
    with open(json_path, "w", encoding="utf-8") as obj:
        json.dump(block_words, obj, ensure_ascii=False, indent=2)


# テスト用の実行コード
# url = "https://www.oca.ac.jp/course/technology/white-hacker/"
# scrape_from_heading(url)
