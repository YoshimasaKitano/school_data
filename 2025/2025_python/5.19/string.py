# string.py
"""
文字列について
文字列は文字が列になったもの
文字'p','あ','ア'
文字列 'python','こんにちは'

"""
msg = "こんにちは"
print(msg) ### こんにちは

msg = 'こんにちは'
print(msg) ### こんにちは

where = "日本"
lang = "Python3"
print(msg,where,lang) ### こんにちは 日本 Python3

print("いわゆる'人工知能'です。") ### いわゆる'人工知能'です。
print('いわゆる"人口知能"です。') ### いわゆる"人口知能"です。

# print("いわゆる"人工知能"です。") ### エラー

## エスケープシーケンス
print("いわゆる\"人工知能\"です。") ### いわゆる"人工知能"です。

# 文字列を改行する
print("選んだ色は\n緑\n黄色")
"""
選んだ色は
緑
黄色
"""

# バックスラッシュを入れる
print("\\") ### \
print("\\100") ### \100

## 複数行の文字列
text = """選んだ色は
緑
黄色
"""
print(text)

## 文字列で使う演算子 + *
a = "Pen"
b = "Apple"

# 文字列連結
pico = a + b + b + a
print(pico) ### PenAppleApplePen

pico = a + b * 2 + a
print(pico) ### PenAppleApplePen

a = "Python"
b = str(3) # str()で数値を文字列に変換する
print(a + b) ### Python3

a = "Python"
b = 3
print(a,b,sep="") ### Python3

"""
練習
高さを表す変数heightに50を代入
底辺を表す変数widthに30を代入
三角形の面積を例のように表示する。

[例]
高さ:50
底辺:30
三角形の
面積は40です。
"""
height = 50
width = 30

print("高さ:" + str(height))
print("底辺:" + str(width))
print("三角形の\n面積は"+ str(round(height * width / 2)) + "です。")
