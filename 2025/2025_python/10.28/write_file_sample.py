### write_file_sample.py
"""
テキストファイルに書き出す
"""
# ファイルの指定
file = "./10.28/sample01.txt"

# ファイルを開く
fileobj = open(file, mode = "a", encoding = "utf-8")

# ファイルに書き込む
fileobj.write("おはようございます。\n")

# ファイルを閉じる
fileobj.close()