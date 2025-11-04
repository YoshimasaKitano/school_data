# lit_sample2.py
"""
リストの要素を操作する
"""
## リストの末尾に要素を追加する append()メソッド
from turtle import color


data = [] # 空のリスト
data.append(10)
print(data) ### [10]

data.append("dog")
print(data) ### [10, 'dog']

data.append(True)
print(data) ### [10, 'dog', True]

## 位置を指定して追加する(挿入する) insert()メソッド
data.insert(1,20) # インデックス番号1の位置に20を挿入する
print(data) ### [10, 20, 'dog', True]

data.insert(3, "cat")
data.insert(5, False)
print(data) ### [10, 20, 'dog', 'cat', True, False]

## リストから要素を抜き取る
# 末尾の要素を抜き取る pop()メソッド
res = data.pop()
print(data) ### [10, 20, 'dog', 'cat', True]
print(res) ### False

# 位置を指定して抜き取る pop(位置)メソッド
res = data.pop(2)
print(data) ### [10, 20, 'cat', True]
print(res) ### dog

# 要素のない位置を指定した場合
# data.pop(4) ### IndexError: pop index out of range

## 要素の値を指定して削除する remove(値)メソッド
res = data.remove(20)
print(data) ### [10, 'cat', True]
print(res) ### None

## インデックス番号を指定して削除する
del data[0]
print(data) ### ['cat', True]

## 変数の存在を抹消する
del data
# print(data) ### NameError: name 'data' is not defined

"""練習
colors = ["red", "yellow", "blue", "green", "pink"]
1.while文を使って colors から末尾から順に要素を抜き取って表示する
2.while文を使って colors から先頭から順に要素をぬきとって表示する
"""
colors = ["red", "yellow", "blue", "green", "pink"]
count = 0
while count < 5:
    res = colors.pop()
    print(res)
    count += 1

colors = ["red", "yellow", "blue", "green", "pink"]
count = 0
while count < 5:
    res = colors.pop(0)
    print(res)
    count += 1

# 解答
colors = ["red", "yellow", "blue", "green", "pink"]
while len(colors) > 0:
    color = colors.pop()
    print(color)

colors = ["red", "yellow", "blue", "green", "pink"]
while len(colors) > 0:
    color = colors.pop(0)
    print(color)

## 文字列とリスト
msg = "may the force be with you!"
words = list(msg)
print(words) ### ['m', 'a', 'y', ' ', 't', 'h', 'e', ' ', 'f', 'o', 'r', 'c', 'e', ' ', 'b', 'e', ' ', 'w', 'i', 't', 'h', ' ', 'y', 'o', 'u', '!']

# 単語を要素にする split()メソッド
words = msg.split() # 空白で区切ってリスト化する
print(words) ### ['may', 'the', 'force', 'be', 'with', 'you!']

time = "12:02"
s = time.split(":") # :で区切ってリスト化する
print(s) ### ['12', '02']

# 文字列をリスト化
color = "red,blue, green,  block"
color = color.replace(" ","") # 半角スペースをスペースなしに置き換える
print(color) ### red,blue,green,block

colors = color.split(",")
print(colors) ### ['red', 'blue', 'green', 'block']

# リストを文字列にする
str_color = ",".join(colors)
print(str_color) ### red,blue,green,block