# tuple_sample1.py
"""
タプル
"""
a = (1, 2, "abc", 3.14, True, (1, "a"))
print(type(a)) ### <class 'tuple'>

b = ("b",)
print(type(b)) ### <class 'tuple'>

# タプルの連結
ab = a + b
print(ab) ### (1, 2, 'abc', 3.14, True, (1, 'a'), 'b')

#タプルは要素の変更、削除、追加ができない
print(ab[2]) ### abc
# ab[2] = "xyz"
print(ab) ### TypeError: 'tuple' object does not support item assignment

# タプルを作る
## 空のタプル
tup = ()
print(type(tup)) ### <class 'tuple'>
print(tup) ### ()

tup = tuple()
print(type(tup)) ### <class 'tuple'>
print(tup) ### ()

## tuple()関数
data = tuple(range(-3, 3)) # 連番のタプル
print(data) ### (-3, -2, -1, 0, 1, 2)

data = tuple("abcde") # 一文字のタプル
print(data) ### ('a', 'b', 'c', 'd', 'e')

li = ["A", "B", "C"]
data = tuple(li) # リストからタプル
print(data) ### ('A', 'B', 'C')

## タプルからリスト
data_list = list(data)
print(data_list) ### ['A', 'B', 'C']

# タプルのスライス
data = ("a", "b", "c", "d", "e", "f", "g")
all = data[:]
print(all) ### ('a', 'b', 'c', 'd', 'e', 'f', 'g')

top3 = data[:3]
print(top3) ### ('a', 'b', 'c')

last3 = data[-3:]
print(last3) ### ('e', 'f', 'g')

skip = data[::2]
print(skip) ### ('a', 'c', 'e', 'g')

reverse = data[::-1]
print(reverse) ### ('g', 'f', 'e', 'd', 'c', 'b', 'a')

# for文を使って要素を表示する
colors = ("red", "blue", "yellow")
for color in colors:
    print(color)
"""
red
blue
yellow
"""

for i, color in enumerate(colors):
    print(i,color)
    data = i, color
    print(data)

"""
0 red
(0, 'red')
1 blue
(1, 'blue')
2 yellow
(2, 'yellow')
"""

# ()を省略
a = 100, 200
print(a) ### (100, 200)
print(type(a)) ### <class 'tuple'>

# タプルのアンパック
a, b = 100, 200
print(a) ### 100
print(b) ### 200

b, a = a, b
print(a) ### 200
print(b) ### 100

data = 10, 20, 30
(a, b, c) = data
print(a) ### 10
print(b) ### 20
print(c) ### 30

# タプルに値が含まれるかを調べる
data = ("a", "b", "c", "d", "e")

print("a" in data) ### True
print("z" in data) ### False

## タプルの集計
numbers = (5, 9, 2, 3, 6)
# 合計
print(sum(numbers)) ### 25

# 最大値
print(max(numbers)) ### 9

# 最小値
print(min(numbers)) ### 2

## タプルの比較
a = (1, 2, 3)
b = (1, 2, 3)

print(a == b) ### True
print(a is b) ### True

c = a
print(a == c) ### True
print(a is c) ### True

d = tuple([1, 2, 3])
print(a == d) ### True
print(a is d) ### False

# 複数のリストを１つにまとめる
x = [1, 2, 3]
y = [4, 5, 6]
z = [7, 8, 9]

zip_obj = zip(x, y, z)
print(zip_obj) ### <zip object at 0x000001A3B90DF240>
print(type(zip_obj)) ### <class 'zip'>

xyz = list(zip_obj)
print(xyz) ### [(1, 4, 7), (2, 5, 8), (3, 6, 9)]

print(list(zip_obj)) ### []

name1 = ["鈴木", "田中", "赤尾"]
name2 = ["星奈", "優美", "恵子"]
zip_obj = zip(name1, name2)

for n1, n2 in zip_obj:
    print(n1 + n2)
"""
鈴木星奈
田中優美
赤尾恵子
"""

for n1, n2 in zip_obj:
    print(n1 + n2)


"""問題
colors = ("red", "blue", "yellow")
"yellow"を"pink"に変更したい

ちなみに...
colors[2] = "pink" # type-error
"""
colors = ("red", "blue", "yellow")
colors = list(colors)
colors.pop()
colors.append("pink")
print(tuple(colors)) ### ('red', 'blue', 'pink')

"""模範解答
"""
colors = ("red", "blue", "yellow")
color_list = list(colors)
color_list[2] = "pink"
colors = tuple(color_list)
print(colors) ### ('red', 'blue', 'pink')