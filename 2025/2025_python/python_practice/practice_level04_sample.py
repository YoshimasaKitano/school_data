### 1. 数値演算子（+, -, *, /, //, %, **）
## 問題1
# 修正して、resultの値を81にする。
# 修正が不要であれば解答は「修正不要」とする。
"""
x = 3
y = 4
z = 2
result = x ** (y | z)
print(result)  # 出力: 81
"""

# 解答
x = 3
y = 4
z = 2
result = x ** (y or z)
print(result)  # 出力: 81


# 解説
# | はビット演算であり、論理演算の or に修正することで、適切な値を選択できます。


## 問題2
# 修正して、resultの値をFalseにする。
# 修正が不要であれば解答は「修正不要」とする。
"""
a = 15
b = 4
result = a % b and a // b
print(result)  # 出力: True
"""

# 解答
a = 15
b = 4
result = bool(a % b and a // b)
print(result)  # 出力: True


# 解説
# bool() を使って演算結果を明確に True または False に変換します。


## 問題3
# 修正して、resultの値をTrueにする。
# 修正が不要であれば解答は「修正不要」とする。
"""
x = 7
y = 2
result = not (x % y)
print(result)  # 出力: True
"""

# 解答
x = 7
y = 2
result = not (x % y == 0)
print(result)  # 出力: True


# 解説
# not を適切な条件と組み合わせることで、True を得られます。


### 2. 文字列演算子（+, *）
## 問題1
# 簡潔な計算に修正して、"PythonPythonPythonPython" を出力する。
# 修正が不要であれば解答は「修正不要」とする。
"""
text = "Python" * 2 + "Python" * 2 and "Python" * 4
print(text)
"""

# 解答
text = "Python" * 4
print(text)  # 出力: PythonPythonPythonPython


# 解説
# and は不要なので削除し、簡潔な計算に修正します。


## 問題2
# 不要なコードを削除して、"Hello!!" を出力する。
# 修正が不要であれば解答は「修正不要」とする。
"""
text = "Hello" + "!" * 2 or "Hello!"
print(text)
"""

# 解答
text = "Hello" + "!" * 2
print(text)  # 出力: Hello!!


# 解説
# or は不要なので削除し、シンプルに計算できるよう修正します。


##問題3
# 修正して、"Python3.12" を出力する。
# 修正が不要であれば解答は「修正不要」とする。
"""
version = 3.12
text = not ("Python" + version)
print(text)
"""

# 解答
version = 3.12
text = "Python" + str(version)
print(text)  # 出力: Python3.12


# 解説
# not は不要なので削除し、数値を文字列化して連結します。



### 3. 比較演算子（==, !=, <, >, <=, >=）
## 問題1
# andをorに変更した場合、演算子を1か所修正して、resultの値をTrueにする。
# 修正が不要であれば解答は「修正不要」とする。
"""
a = 10
b = 5
result = a == b and b > a
print(result) # 出力: False 
"""

# 解答
a = 10
b = 5
result = a == b or b < a
print(result)  # 出力: True


# 解説
# and を or にし、正しい比較演算を適用します。


## 問題2
# resultの値をFalseに評価できるよう修正します。
# 修正が不要であれば解答は「修正不要」とする。
"""
x = 7
y = 7
result = not (x != y and y >= x)
print(result) # 出力: True
"""

# 解答
x = 7
y = 7
result = not (x != y or y >= x)
print(result) # 出力: False


# 解説
# and を or に変更し、条件を正しく評価できるよう修正します。


## 問題3
# 修正して、resultの値をFalseにする。
# 修正が不要であれば解答は「修正不要」とする。
"""
val1 = 10
val2 = 20
result = val1 > val2 or val2 and val1
print(result)
"""

# 解答
val1 = 10
val2 = 20
result = val1 > val2 and bool(val2)
print(result)  # 出力: False


# 解説
# or を and に修正し、bool() を使用して値の状態を明確にしました。
