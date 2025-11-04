### write_file_sample.py
"""
テキストファイルに書き出す
with-as
"""
# ファイルの指定
file = "./10.28/sample02.txt"

# ファイルを開く
with open(file, mode = "w", encoding = "utf-8") as fileobj:

    # ファイルに書き込む
    fileobj.write("おはようございます。\n")
    fileobj.write("こんにちは。\n")
    fileobj.write("お疲れさまでした。\n")