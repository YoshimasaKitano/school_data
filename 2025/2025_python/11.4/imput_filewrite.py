### input_fileewrite.py
"""
入力した内容をファイルの先頭に追記する
"""
# ファイルの指定
file = "./11.4/data/sample.txt"

# 入力
newtext = input("追加する内容を入力:")

text = ""

try: # 初回にファイルがない場合にエラーになる
    # ファイルのデータをすべて取得する
    with open(file, "r", encoding = "utf-8") as fileobj:
        text = fileobj.read()

except:
    print("ファイルがありません。")

# 新しいデータと既存データをつないで保存する
with open(file, "w", encoding = "utf-8") as fileobj:
    fileobj.write(newtext + "\n") # 新しいデータと改行コード
    fileobj.write(text)

print("追記しました。")