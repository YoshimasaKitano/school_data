### exists_test.py
"""
フォルダがなければ作成
ファイルがあれば上書きするか確認
"""
# モジュール
import os # OSを操作するモジュール
from random import randint

# pathの指定
folder = "./11.4/data/"
file = folder + "sample.txt"

# ファイルを保存する関数の定義
def filewrite():
    # フォルダの確認
    if not os.path.exists(folder): # ない場合
        os.makedirs(folder) # フォルダを作る

    # ファイルに書き込む
    with open(file, "w", encoding = "utf-8") as fileobj:
        num = randint(0, 100)
        fileobj.write(f"{num}が出ました。")
        print("ファイルに保存しました。")

# ファイルがあるか確認する
if os.path.exists(file): # ファイルがある場合

    while True:
        answer = input("上書きしてもよいですか？(y/n)")
        if answer == "y":
            filewrite()
            break
        elif answer == "n":
            break
else:
    filewrite()
