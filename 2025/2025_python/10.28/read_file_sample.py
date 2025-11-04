### read_file_sample.py
"""
テキストファイルのデータを読み込む
"""

# 読み込むファイルのpathを指定
file = "./10.28/fox.txt" # ルートディレクトリからの絶対パス

# ファイルを開く
fileobj = open(file, mode="r", buffering=1, encoding="utf-8", )

# ファイルオブジェクトからデータを読み込む
text = fileobj.read()

# ファイルを閉じる
fileobj.close()

print(text)