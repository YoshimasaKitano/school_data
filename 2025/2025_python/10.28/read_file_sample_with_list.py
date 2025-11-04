### read_file_sample_with_list.py
"""
テキストファイルのデータを読み込む
with-as文
読み込んだデータをリスト化:単語リストを作る
"""

# 読み込むファイルのpathを指定
file = "./10.28/fox.txt" # ルートディレクトリからの絶対パス

# ファイルを開いてファイルオブジェクトを作る
with open(file, mode="r", buffering=1, encoding="utf-8", ) as fileobj:

    # ファイルオブジェクトからデータを読み込む
    text = fileobj.read()

    # 末尾のピリオドを取り除く
    newText = text.rstrip(".")

    # スペースで切り分ける
    wordlist = newText.split(" ")

    print(wordlist)