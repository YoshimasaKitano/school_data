# method.py
"""
オブジェクトのメソッド
"""
s = "Hello Python"

## 値の型を調べる関数
res = type(s)
print(res) ### <class 'str'>

## 文字列の文字を大文字にするメソッド
res = s.upper()
print(res) ### HELLO PYTHON

res = "123".upper()
print(res) ### 123

## 文字列のメソッド
s = "Apple iPhone と Google Android"

# 文字列を小文字にするメソッド
print(s.lower()) ### apple iphone と google android

# 小文字を大文字に、大文字を小文字にする swapcase()
print(s.swapcase()) ### aPPLE IpHONE と gOOGLE aNDROID

print(s) ### Apple iPhone と Google Android

print(s) ### apple iphone と google android

# 文字列の最初の文字だけ大文字にする capitalize()
print(s.capitalize()) ### Apple iphone と google android

# 各単語の頭文字を大文字にする title()
print(s.title()) ### Apple Iphone と Google Android

# 文字数を調べる関数 len()
print(len(s)) ### 29

# 文字列に含まれる個数を検索するメソッド count()
print(s.count("p")) ### 3 # "p"がいくつあるか

print(s.count("p",6)) ### 1
print(s[6:].count("p")) ### 1

print(s.count("p",6,12)) ### 1
print(s[6:12].count("p")) ### 1

print(s.count("google")) ### 1

# 文字列を検索して最初の位置を返す find()
print(s.find("le")) ### 3
print(s.find("x")) ### -1 # 見つからなかった場合

print(s.find("le", 0 , 12)) ### 3 # インデックス番号の0から12までの範囲で"le"を検索

# 文字を後ろから検索して最初の位置(インデックス番号)を返す rfind()
print(s.rfind("le")) ### 19

# 文字列を置換する replace()
print(s.replace("p","q")) # (置換前,置換後) ### Aqqle iPhone と Google Android
print(s.replace("と","か"))### Apple iPhone か Google Android
print(s.replace("と","and"))### Apple iPhone and Google Android

print(s) ### Apple iPhone と Google Android
s_replace = s.replace("と","and")
print(s_replace) ### Apple iPhone and Google Android

# 置き換える数を指定する
print(s.replace("o","O",2)) ### Apple iPhOne と GOogle Android

# 前後の余分な文字を取り除く strip()
t = "  hello  \n"
print(t.strip()) ### hello

t = "aa_helalo_aa"
print(t.strip("a")) ### _helalo_

file_name = "image.jpg"
name = file_name.strip(".jpg")
print(name) ### image

# 複数指定して取り除く
t = "dog.peg.jpg"
print(t.rstrip(".jpeg")) ### do


# 文字列に値を埋め込む format()
s = "チューリップは、{}と{}と{}でした。"
print(s.format("赤","青","黄色")) ### チューリップは、赤と青と黄色でした。
print("チューリップは、{}と{}と{}でした。".format("黄色","赤","青")) ### チューリップは、黄色と赤と青でした。

# 変数を使う
color1 = "赤"
color2 = "青"
color3 = "黄色"
print(s.format(color1,color2,color3)) ### チューリップは、赤と青と黄色でした。

# 番号を指定する
print("チューリップは、{1}と{2}と{0}でした。".format("黄色","赤","青")) ### チューリップは、赤と青と黄色でした。

# キーワード引数を使う
print("チューリップは、{c1}と{c2}と{c0}でした。".format(c0="黄色",c1="赤", c2="青")) ### チューリップは、赤と青と黄色でした。

# f-stringsの記述
c1 = "赤"
c2 = "青"
c3 = "黄色"

print(f"チューリップは、{c1}と{c2}と{c3}でした。") ### チューリップは、赤と青と黄色でした。


# 書式の指定
"""
3桁位取り
10000円 → 10.000円
"""
tokyo = 123456000
kyoto = 53900

print(f"東京:{tokyo:,}、京都:{kyoto:,}") ### 東京:123,456,000、京都:53,900

s = "東京:{:,}、京都:{:,}、その他:{:,}"
print(s.format(tokyo,kyoto,10000000)) ### 東京:123,456,000、京都:53,900、その他:10,000,000


# 小数点以下の桁数を指定する
length = 25.34
thickness = 5.62

text = f"長さ:{length:.1f}cm、厚み:{thickness:.0f}mm"
print(text) ### 長さ:25.3cm、厚み:6mm

num = 12345.0321
print(f"{num:,.2f}") ### 12,345.03

# 値の位置を揃える(左詰め、中央揃え、右詰め)
num1 = 123.4
num2 = 56.7
num3 = 3040.1

print(num1)
print(num2)
print(num3)
"""
123.4
56.7
3040.1
"""
print(f"{num1:>10.1f}")
print(f"{num2:>10.1f}")
print(f"{num3:>10.1f}")
"""
     123.4
      56.7
    3040.1
"""
