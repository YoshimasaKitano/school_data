# list_sample.py
"""練習問題
文字列 TeacherのTをRに入れ替える
・replace()使わない
・文字列のスライスも使用しない
"""
# リストを使った場合
## 文字列をリスト化する
text = list("Teacher")

## 要素を置き換える
text[0] = "R"

## リストの要素をつないで文字列にする
text_str = "".join(text)

## 出力する
print(text_str) ### Reacher

"""replace()を使った場合
str = "Teacher"
str2 = str.replace("T","R")
print(str2) ### Reacher
"""

"""スライスを使った場合
str = str[1::]
str2 = "R" + str
print(str2) ### Reacher
"""

"""
リストの連結
"""
# 文字列演算子を使って連結
abc = ["a", "b", "c"]
xyz = ["x", "y", "z"]

az = abc + xyz
print(az) ### ['a', 'b', 'c', 'x', 'y', 'z']

az += abc
print(az) ### ['a', 'b', 'c', 'x', 'y', 'z', 'a', 'b', 'c']

# リストの要素にリストを追加する extend()メソッド
abc.extend(xyz)
print(abc) ### ['a', 'b', 'c', 'x', 'y', 'z']

## append()メソッド リストに要素を追加する
abc = ["a", "b", "c"]
abc.append(xyz)
print(abc) ### ['a', 'b', 'c', ['x', 'y', 'z']]

"""
リストをスライスする
"""
str = ["a", "b", "c", "d", "e", "f", "g"]
print(str[:]) ### ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(str[4:]) ### ['e', 'f', 'g']
print(str[:4]) ### ['a', 'b', 'c', 'd']
print(str[2:6]) ### ['c', 'd', 'e', 'f']
print(str[::2]) ### ['a', 'c', 'e', 'g']
print(str[::-1]) ### ['g', 'f', 'e', 'd', 'c', 'b', 'a']

"""
リストの比較
"""
# リストの要素の比較
str_A = ["a", "b", "c"]
str_B = ["a", "b", "c"]
str_C = ["c", "b", "a"]

print(str_A == str_B) ### True
print(str_A == str_C) ### False

str_D = str_A
print(str_A == str_D) ### True
print(str_B == str_D) ### True

# オブジェクトの比較
print(str_A is str_B) ### False
print(str_A is str_D) ### True

print(str_A is not str_B) ### True

str_D.append("d")
print(str_D) ### ['a', 'b', 'c', 'd']
print(str_A is str_D) ### True
print(str_A) ### ['a', 'b', 'c', 'd']

# 複製 copy()メソッド
str_E = str_C.copy()
print(str_E) ### ['c', 'b', 'a']
print(str_E == str_C) ### True
print(str_E is str_C) ### False

# スライス
str_F = str_C[:]
print(str_F) ### ['c', 'b', 'a']
print(str_F == str_C) ### True
print(str_F is str_C) ### False

# list()関数
str_G = list(str_C)
print(str_G) ### ['c', 'b', 'a']
print(str_G == str_C) ### True
print(str_G is str_C) ### False

### 文字列
a = "abcde"
b = "abcde"
c = "edcba"
print(a == b) ### True
print(a == c) ### False

print(a is b) ### True

d = a
print(a == d) ### True
print(a is d) ### True

# e = a.copy()　### AttributeError: 'str' object has no attribute 'copy'
f = a[:]
print(a == f) ### True
print(a is f) ### True