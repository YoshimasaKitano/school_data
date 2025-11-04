### asksave_text.py
"""
ファイルダイアログで保存先を指定する
"""
import tkinter as tk
import tkinter.filedialog as fd
from random import random

root = tk.Tk()
root.withdraw()

# 書き出すデータの作成
def getdata():
    num = random()
    return str(num)

file = fd.asksaveasfilename(
    initialfile = "mydata",
    defaultextension = ".txt",
    title = "保存場所を指定",
    filetypes = [("テキスト", ".txt")]
)

savedata = getdata()
print(savedata)

# 書き込み
if file:
    with open(file, "w", encoding = "utf-8") as fileobj:
        length = fileobj.write(savedata)
        print(f"{length}文字保存しました。")