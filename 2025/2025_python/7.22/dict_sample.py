# dict_sample.py
"""
辞書(dict)
{キー : 値, キー : 値, キー : 値,}
"""
from tkinter import Y


stock = {"S":7, "M":12, "L":3}
print(stock["S"]) ### 7
print(stock["M"]) ### 12
print(stock["L"]) ### 3

# print(stock[0]) ### KeyError: 0

data = {(1, "a"):["ab", "cd"], (2, "b"):["ef", "gh"]}
print(data[(1, "a")]) ### ['ab', 'cd']

metro = {
    "M":"御堂筋線", 
    "Y":"四つ橋線", 
    "S":"千日前線", 
    "C":"中央線",
    "K":"堺筋線",
    "T":"谷町線",
    "N":"長堀鶴見緑地線",
    "I":"今里筋線",
    "P":"ニュートラム", 
    }
print(metro) ### {'M': '御堂筋線', 'Y': '四つ橋線', 'S': '千日前線', 'C': '中央線', 'T': '谷町線', 'N': '長堀鶴見緑地線', 'I': '今里筋線', 'P': 'ニュ ートラム'}
print(metro["Y"]) ### 四つ橋線
print(metro["N"]) ### 長堀鶴見緑地線

# 辞書の要素の数
print(len(metro)) ### 9

# 辞書の型
print(type(metro)) ### <class 'dict'>

# 辞書を作る dict()関数
## タプル(キー, 値)を要素に持つリストから辞書を作る
list_data = [("yellow", 3), ("blue", 6), ("green", 5)]
dict_data = dict(list_data)
print(dict_data) ### {'yellow': 3, 'blue': 6, 'green': 5}
print(dict_data["blue"]) ### 6

## 2つのリストをzipして辞書を作る
keys = ["yellow", "blue", "green"]
values = [3, 6, 5]
zip_obj = zip(keys, values)
print(zip_obj) ### <zip object at 0x000001F846B6F100>
# for t in zip_obj:
#     print(t)
"""
('yellow', 3)
('blue', 6)
('green', 5)
"""
dict_data = dict(zip_obj)
print(dict_data) ### {'yellow': 3, 'blue': 6, 'green': 5}

## リストを要素にもつタプルから辞書を作る
tuple_data = (["yellow", 3], ["blue", 6], ["green", 5])
dict_data = dict(tuple_data)
print(dict_data) ### {'yellow': 3, 'blue': 6, 'green': 5}

## タプルを要素に持つタプルから辞書を作る
tuple_data = (("yellow", 3), ("blue", 6), ("green", 5))
dict_data = dict(tuple_data)
print(dict_data) ### {'yellow': 3, 'blue': 6, 'green': 5}


## キーワード引数を利用する
dict_data = dict(yellow = 3, blue = 6, green = 5)
print(dict_data) ### {'yellow': 3, 'blue': 6, 'green': 5}

# 初期値から辞書を作る fromkeys()メソッド
stock_list = ["S", "M", "L"]

# 初期値を指定した場合
stock = dict.fromkeys(stock_list, 0)
print(stock) ### {'S': 0, 'M': 0, 'L': 0}

# 初期値を指定してなかった場合
stock = dict.fromkeys(stock_list)
print(stock) ### {'S': None, 'M': None, 'L': None}

# 空の辞書を作る
empty_dict = {}
print(empty_dict) ### {}
print(type(empty_dict)) ### <class 'dict'>

empty_dict = dict()
print(empty_dict) ### {}
print(type(empty_dict)) ### <class 'dict'>

# 辞書の要素の更新と削除
dict_data = {"yellow":3, "blue":6, "green":5}

## 更新
dict_data["blue"]= 10
dict_data["green"] = 2
print(dict_data) ### {'yellow': 3, 'blue': 10, 'green': 2}

### 存在しないキーを指定した場合は追加される
dict_data["black"] = 20
print(dict_data) ### {'yellow': 3, 'blue': 10, 'green': 2, 'black': 20}

"""練習問題
文字列「たけやぶやけた」
文字をキー、登場回数を値とする辞書を作成する
"""
t = 0
k = 0
y = 0
b = 0
dict_data = {}
for s in "たけやぶやけた":
    if s == "た":
        t += 1
    elif s == "け":
        k += 1
    elif s == "や":
        y += 1
    else:
        b += 1
dict_data["た"] = t
dict_data["け"] = k
dict_data["や"] = y
dict_data["ぶ"] = b
print(dict_data)

"""模範解答
"""
text = "たけやぶやけた"
dict_data = {}
for s in text:
    dict_data[s] = text.count(s)

print(dict_data)

# キーがあればそのまま、なければ追加する setdefault()メソッド
dict_data = {"yellow":3, "blue":6, "green":5}

## キーがあればそのまま何もしない
dict_data.setdefault("blue", 30)
print(dict_data) ### {'yellow': 3, 'blue': 6, 'green': 5}

## キーがなければ追加する
dict_data.setdefault("red", 5)
print(dict_data) ### {'yellow': 3, 'blue': 6, 'green': 5, 'red': 5}

text = "たけやぶやけた"
dict_data = {}
for s in text:
    dict_data.setdefault(s, text.count(s))

print(dict_data)

# 要素を追加する
number = {} # 空の辞書
number["one"] = 1
number["two"] = 2
number["three"] = 3
print(number) ### {'one': 1, 'two': 2, 'three': 3}

# 他の辞書で要素を更新する update()メソッド
data = {"a":10, "b":20, "c":30}
newdata = {"a":15, "d":40}

data.update(newdata)
print(data) ### {'a': 15, 'b': 20, 'c': 30, 'd': 40}

# 要素を削除する
dict_data = {"yellow":3, "blue":6, "green":5}

## キーを指定して要素を削除
del dict_data["yellow"] # キーを指定する
print(dict_data) ### {'blue': 6, 'green': 5}

# 存在しないキーを指定した場合
# del dict_data["yellow"] # KeyError: 'yellow'

## 要素をすべて削除する clear()メソッド
dict_data.clear()
print(dict_data) ### {}

## データを破棄する
dict_data = {"yellow":3, "blue":6, "green":5}
del dict_data # データを破棄する
# print(dict_data) ### NameError: name 'dict_data' is not defined. Did you mean: 'list_data'?

# 辞書内包表記
keys = ["a", "b", "c", "d"]
dict_data = {}
for k in keys:
    dict_data[k] = 10

print(dict_data) ### {'a': 10, 'b': 10, 'c': 10, 'd': 10}

## 辞書内包表記
keys = ["a", "b", "c", "d"]
dict_data = {k:10 for k in keys}

print(dict_data) ### {'a': 10, 'b': 10, 'c': 10, 'd': 10}

"""練習
以下のコードを辞書内包表記で記述する
"""
text = "たけやぶやけた"
dict_data = {s:text.count(s) for s in text}

print(dict_data) ### {'た': 2, 'け': 2, 'や': 2, 'ぶ': 1}

"""練習
文字列「python」から
文字をキー、インデックス番号を値とする辞書を辞書内包表記で作る
"""
text = "python"
dict_text = {k:i for i, k in enumerate(text)}
print(dict_text) ### {'p': 0, 'y': 1, 't': 2, 'h': 3, 'o': 4, 'n': 5}

# 辞書を複製する
data = {"a":10, "b":20, "c":30}

## 代入する
data_a = data
print(data_a) ### {'a': 10, 'b': 20, 'c': 30}
print(data == data_a) ### True
print(data is data_a) ### True # オブジェクトが同じ

data_a["d"] = 40
print(data_a) ### {'a': 10, 'b': 20, 'c': 30, 'd': 40}
print(data) ### {'a': 10, 'b': 20, 'c': 30, 'd': 40}

## コピーする
data = {"a":10, "b":20, "c":30}

data_b = data.copy()
print(data_b) ### {'a': 10, 'b': 20, 'c': 30}
print(data == data_b) ### True
print(data is data_b) ### False # オブジェクトが違う

data_b["d"] = 40
print(data_b) ### {'a': 10, 'b': 20, 'c': 30, 'd': 40}
print(data) ### {'a': 10, 'b': 20, 'c': 30}

# 同じ構造の辞書を作る
data = {"a":10, "b":20, "c":30}
data2 = dict.fromkeys(data, 0)
print(data2) ### {'a': 0, 'b': 0, 'c': 0}