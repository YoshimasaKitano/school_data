## 1. 数値演算子（+, -, *, /, //, %, **）
## 問題1
# 演算子を1か所修正して、resultの値を36にする
# 修正が不要であれば解答は「修正不要」とする。
"""
x = 6
result = x ^ 2
print(result)  # 出力: 36
"""
# 解答
x = 6
result = x ** 2
print(result) ### 36


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
print(result) ### 4.0




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
print(result) ### 1


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
print(text)


## 問題5
# 修正して、"Python3.12" を出力する。
# 修正が不要であれば解答は「修正不要」とする。
"""
version = 3.12
text = "Python" + version
print(text)
"""
# 解答
version = "3.12"
text = "Python" + version
print(text)


## 問題6
# 修正して、"ABABAB" を出力する
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
print(result)


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
result = a <= b
print(result)



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
print(result)


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
print(result)


