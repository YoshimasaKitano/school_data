# set_sample1.py
"""
セット(集合)
"""
setA = {"blue", "yellow", "red"}
setB = {"green", "blue", "black"}

print(setA) ### {'red', 'blue', 'yellow'}
print(type(setA)) ### <class 'set'>
print(setB) ### {'blue', 'black', 'green'}
print(type(setB)) ### <class 'set'>

# セットの和集合 |
# color_set = setA + setB ### ### TypeError: unsupported operand type(s) for +: 'set' and 'set'
color_set = setA | setB
print(color_set) ### {'green', 'black', 'yellow', 'red', 'blue'}

# 要素の数
print(len(color_set)) ### 5

# in演算子
print("red" in color_set) ### True
print("white" in color_set) ### False
print("blue" not in color_set) ### False

# 空のセットを作る
li = []
print(li) ### []

tup = ()
print(tup) ### ()

se = {}
print(se) ### {}
print(type(se)) ### <class 'dict'> 辞書型

s = set()
print(s) ### set()
print(type(s)) ### <class 'set'> セット型

# set()でセットを作る
num_set = set(range(5))
print(num_set) ### {0, 1, 2, 3, 4}

num_set = set(range(4, -3, -1))
print(num_set) ### {0, 1, 2, 3, 4, -2, -1}

set_data = {1}
print(set_data) ### {1}
print(type(set_data)) ### <class 'set'>

# セットには重複した値がない
set_data = {1, 3, 6, 2, 8, 6, 7, 5, 1, 3}
print(set_data) ### {1, 2, 3, 5, 6, 7, 8}

# リストからセット
set_data = set(["a", "b", "c"])
print(set_data) ### {'b', 'a', 'c'}

# セットにはインデックス番号がない
# print(set_data[0]) ### TypeError: 'set' object is not subscriptable

# セットからリスト
list_data = list(set_data)
print(list_data) ### ['c', 'b', 'a']
print(type(list_data)) ### <class 'list'>

# 文字列からセット
set_data = set("happy")
print(set_data) ### {'y', 'h', 'p', 'a'}

# セットから文字列
s = "".join(set_data)
print(s) ### hapy