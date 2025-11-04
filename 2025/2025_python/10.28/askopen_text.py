### askopen_text.py

"""
ファイルダイアログを開いて読み込むファイルを指定する
"""
# Tkinterライブラリの読み込み
import tkinter as tk
import tkinter.filedialog as fd # ファイルダイアログのモジュール

root = tk.Tk() # Tkinterのオブジェクトを生成
root.withdraw() # Tkinterのウィンドウ非表示

file = fd.askopenfilename(
    title = "ファイルを選んでください。",
    filetypes = [("TEXT", ".txt"), ("TEXT", ".py"), ("HTML", ".html")]
)

print(file)

if file: # fileに値がある場合
    # ファイルを開いてデータを読み込む
    with open(file, "r", encoding = "utf-8") as fileobj:
        text = fileobj.read(10) # read(文字数指定)

        print(text)