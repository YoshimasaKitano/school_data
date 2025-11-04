# built_in_func.py
"""
組み込み関数:初めから用意されている関数
関数名(引数)
引数は１つしか入れることができない関数もあれば、
複数の引数を入れることができる関数もある。

"""
print("表示する関数") ### 表示する関数
type("データ型を示す関数")
str("文字列型に変換する関数")

## 数値計算に使う関数
# abs(数値)絶対値を返す
print(abs(3 )) ### 3
print(abs(-3)) ### 3

# max() 引数の最大値を返す
print(max(5,9,-2,1,-3)) ### 9

# min() 引数の最小値を返す
print(min(5,9,-2,1,-3)) ### -3

# pow(x,y) xのy乗を返す
print(pow(2,3)) ### 8

# pow(x,y,z) xのy乗をzで割ったあまりを返す
print(pow(2,3,5)) ### 3

# round() 引数の値のまるめ処理結果を返す
print(round(3.65)) ### 4

print(round(3.65,1)) ### 3.6
print(round(3.65,2)) ### 3.65

## 文字列に使う関数
# len() 引数の文字列の文字数を返す
print(len("Python")) ### 6
print(len("おはようございます")) ### 9

# chr() 引数のUnicodeを文字列で返す
print(chr(97)) ### a

# ord() 引数の文字をUnicodeで返す
print(ord("a")) ### 97
# print(ord("おはよう")) ### TypeError

print(ord("北")) ### 21271
print(ord("野")) ### 37326
print(chr(21271) + chr(37326)) ### 北野

## 入力に使う関数
# input() キーボードからの入力を取得
# 入力されたデータは文字列型で取得する
s = input("入力→")
print(type(s)) ### <class 'str'>
print(s)
print(s * 3)
