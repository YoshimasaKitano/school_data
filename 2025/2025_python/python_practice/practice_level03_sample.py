### 1. 数値演算子（+, -, *, /, //, %, **）
## 問題1
# 演算子を1か所修正して、resultの値を64にする。
# 修正が不要であれば解答は「修正不要」とする。
"""
x = 2
y = 3
z = 4
result = x ** y * z ^ 2
print(result)  # 出力: 64
"""

# 解答
x = 2
y = 3
z = 4
result = x ** y * z * 2
print(result)  # 出力: 64


## 問題2
# 演算子を1か所修正して、resultの値を6にする。
# 修正が不要であれば解答は「修正不要」とする。
"""
a = 15
b = 4
result = a / b - a % b
print(result)  # 出力: 6
"""

# 解答
a = 15
b = 4
result = a // b + a % b
print(result)  # 出力: 6


## 問題3
# 演算子を1か所修正して、resultの値を4.5にする。
# 修正が不要であれば解答は「修正不要」とする。
"""
x = 7
y = 2
result = x / y + x // y
print(result)  # 出力: 4.5
"""

# 解答
x = 7
y = 2
result = x / y + x % y
print(result)  # 出力: 4.5


### 2. 文字列演算子（+, *）
## 問題1
# 修正して、"HelloHelloHello!" を出力する。
# 修正が不要であれば解答は「修正不要」とする。
"""
text = "Hello" * 3 + "!"
print(text)
"""

# 解答
text = ("Hello" * 3) + "!"
print(text)  # 出力: HelloHelloHello!


# 解説
# 演算子の優先順位を明確にするため、繰り返し部分を括弧で囲みます。


## 問題2
# 修正して、"Python3.1" を出力する。
# 修正が不要であれば解答は「修正不要」とする。
"""
version = 3.12
text = "Python" * str(version)
print(text)
"""

# 解答
version = 3.12
text = "Python" + str(version)
print(text)  # 出力: Python3.12


# 解説
# * ではなく + を使用して文字列を結合します。


## 問題3
# 修正して、"XYZXYZXYZ" を出力する。
# 修正が不要であれば解答は「修正不要」とする。
"""
text1 = "X"
text2 = "Y"
text3 = "Z"
result = text1 + text2 + text3 * 3
print(result)
"""

# 解答
text1 = "X"
text2 = "Y"
text3 = "Z"
result = (text1 + text2 + text3) * 3
print(result)  # 出力: XYZXYZXYZ


# 解説
# 繰り返しの対象を括弧で囲み、全体を3回繰り返します。


### 3. 比較演算子（==, !=, <, >, <=, >=）
## 問題1
# 修正して、resultの値をTrueにする。
# 修正が不要であれば解答は「修正不要」とする。
"""
x = 10
y = 5
result = x != y
print(result)
"""

# 解答
x = 10
y = 5
result = x >= y
print(result)  # 出力: True



## 問題2
# 修正して、resultの値をFalseにする。
# 修正が不要であれば解答は「修正不要」とする。
"""
a = 7
b = 7
result = a =! b
print(result)
"""

# 解答
a = 7
b = 7
result = a != b
print(result)  # 出力: False



## 問題3
# 修正して、resultの値をTrueにする。
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
print(result)  # 出力: True


