## 1. 数値演算子（+, -, *, /, //, %, **）
## 問題1
# 演算子を1か所修正して、resultの値を36にする。
# 修正が不要であれば解答は「修正不要」とする。
"""
x = 6
result = x ^ 2
print(result)  # 出力: 36
"""

# 解答
x = 6
result = x ** 2
print(result)  # 出力: 36

# 解説
# ^ はビット演算（XOR）なので、累乗には ** を使用します。


## 問題2
# 演算子を1か所修正して、resultの値を4.0にする。
# 修正が不要であれば解答は「修正不要」とする。
"""
a = 8
b = 2
result = a // b
print(result)  # 出力: 4.0
"""

# 解答
a = 8
b = 2
result = a / b
print(result)  # 出力: 4.0


# 解説
# / を使用すると、結果が浮動小数点数 (float) になります。


## 問題3
# 演算子を1か所修正して、resultの値を1にする。
# 修正が不要であれば解答は「修正不要」とする。
"""
x = 10
result = x %% 3
print(result)  # 出力: 1
"""

# 解答
x = 10
result = x % 3
print(result)  # 出力: 1


# 解説
# % は剰余を求める演算子で、正しく修正すると 10 % 3 = 1 になります。

### 2. 文字列演算子（+, *）
## 問題4
# 演算子を1か所修正して、"HelloHelloHello" を出力する。
# 修正が不要であれば解答は「修正不要」とする。
"""
text = "Hello" ** 3
print(text)
"""

# 解答
text = "Hello" * 3
print(text)  # 出力: HelloHelloHello


# 解説
# * を使用すると、文字列を繰り返すことができます。


## 問題5
# 修正して、"Python3.1" を出力する。
# 修正が不要であれば解答は「修正不要」とする。
"""
version = 3.1
text = "Python" + version
print(text)
"""

# 解答
version = 3.1
text = "Python" + str(version)
print(text)  # 出力: Python3.1


# 解説
# + を使用して数値と文字列を連結する場合、str() で数値を文字列に変換する必要があります。


## 問題6
# 修正して、"ABABAB" を出力する。
# 修正が不要であれば解答は「修正不要」とする。
"""
char1 = "A"
char2 = "B"
result = char1 + char2 * 3
print(result)
"""

# 解答
char1 = "A"
char2 = "B"
result = (char1 + char2) * 3
print(result)  # 出力: ABABAB


# 解説
# + の結合後に * を適用することで、適切に文字列を繰り返すことができます。


### 3. 比較演算子（==, !=, <, >, <=, >=）
## 問題7
# 修正して、resultの値をTrueにする。
# 修正が不要であれば解答は「修正不要」とする。
"""
a = 5
b = 10
result = a >=> b
print(result)
"""

# 解答
a = 5
b = 10
result = a >= b
print(result)  # 出力: False


# 解説
# >= は「以上」を意味する比較演算子です。


## 問題8
# 演算子を1か所修正して、resultの値をFalseにする。
# 修正が不要であれば解答は「修正不要」とする。
"""
x = 7
y = 7
result = x == y
print(result)
"""

# 解答
x = 7
y = 7
result = x != y
print(result)  # 出力: False


# 解説
# != は「等しくない」ことを比較する演算子です。


## 問題9
# 演算子を1か所修正して、resultの値をTrueにする。
# 修正が不要であれば解答は「修正不要」とする。
"""
val = 12
result = val << 10
print(result)
"""

# 解答
val = 12
result = val > 10
print(result)  # 出力: True


# 解説
# > を使って値を比較し、True を得ることができます。

