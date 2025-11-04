### 1. 数値演算子（+, -, *, /, //, %, **）
## 問題1
# 演算子を1か所修正して、resultの値を27にする。
# 修正が不要であれば解答は「修正不要」とする。
"""
x = 3
result = x ^ 3
print(result)
"""
# 解答
x = 3
result = x ** 3
print(result)



## 問題2
# 演算子を1か所修正して、resultの値を1.5にする
# 修正が不要であれば解答は「修正不要」とする。
"""
a = 9
b = 6
result = a // b
print(result)
"""
# 解答
a = 9
b = 6
result = a / b
print(result)



## 問題3
# 演算子を1か所修正して、resultの値を2にする
# 修正が不要であれば解答は「修正不要」とする。
"""
x = 22
y = 5
result = x // y - x // y
print(result)
"""
# 解答
x = 22
y = 5
result = x // y - x % y
print(result)


### 2. 文字列演算子（+, *）
## 問題1
# 修正して、"PythonPythonPython" を出力する
# 修正が不要であれば解答は「修正不要」とする。
"""
text = "Python" ** 3
print(text)
"""
# 解答
text = "Python" * 3
print(text)


## 問題2
# 修正して、"Hello World!" を出力する
# 修正が不要であれば解答は「修正不要」とする。
"""
text1 = "Hello"
text2 = "World!"
result = text1 + text2
print(result)
"""
# 解答
text1 = "Hello"
text2 = "World!"
print(text1,text2,sep=" ")


## 問題3
# 修正して、"ABABABAB" を出力する
# 修正が不要であれば解答は「修正不要」とする。
"""
char1 = "A"
char2 = "B"
result = char1 + char2 * 4
print(result)
"""
# 解答
char1 = "A"
char2 = "B"
result = (char1 + char2) * 4
print(result)


### 3. 比較演算子（==, !=, <, >, <=, >=）
## 問題1
# 演算子を1か所修正して、resultの値をTrueにする
# 修正が不要であれば解答は「修正不要」とする。
"""
x = 10
y = 15
result = x =! y
print(result)
"""
# 解答
x = 10
y = 15
result = x != y
print(result)


## 問題2
# 修正して、resultの値をFalseにする
# 修正が不要であれば解答は「修正不要」とする。
"""
a = 7
b = 7
result = a == b
print(result)
"""
# 解答
a = 7
b = 7
result = a != b
print(result)


## 問題3
# 修正して、resultの値をTrueにする
# 修正が不要であれば解答は「修正不要」とする。
"""
x = 20
y = 15
result = x >> 1
print(result)
"""
# 解答
x = 20
y = 15
result = x > y
print(result)

