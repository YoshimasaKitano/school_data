### read_file_sample_with.py
"""
テキストファイルのデータを読み込む
with-as文
"""

# 読み込むファイルのpathを指定
file = "./10.28/fox.txt" # ルートディレクトリからの絶対パス

# ファイルを開いてファイルオブジェクトを作る
with open(file, mode="r", buffering=1, encoding="utf-8", ) as fileobj:

    # ファイルオブジェクトからデータを読み込む
    text = fileobj.read()

    print(text)