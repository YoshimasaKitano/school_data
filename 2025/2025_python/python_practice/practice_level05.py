### 1. 数値演算とビット演算の組み合わせ
## 問題
# 「result = x << y + x ** 2」を修正して、resultの値を48にする。
# 修正が不要であれば解答は「修正不要」とする。
"""
x = 4
y = 3
result = x << y + x ** 2
print(result)  
"""


### 2. ビット演算と論理演算
## 問題
# 「result = (a & b) or (a ^ b)」を修正して、resultの値をTrueにする
# 修正が不要であれば解答は「修正不要」とする。
"""
a = 12
b = 10
result = (a & b) or (a ^ b)
print(result)
"""


### 3. 文字列操作と論理演算
## 問題
# 「result = text1 and text2」を修正して、resultの値を"Yes"にする
# 修正が不要であれば解答は「修正不要」とする。
"""
text1 = "Yes"
text2 = "No"
result = text1 and text2
print(result)  
"""



### 4. 数値演算と比較演算
## 問題
# 「result = x > y and x << 1 == y」を修正して、resultの値をTrueにする
# 修正が不要であれば解答は「修正不要」とする。
"""
x = 8
y = 16
result = x > y and x << 1 == y
print(result)  # 出力: False
"""



### 5. ビット演算と文字列操作
## 問題
# 「result = char1 + char2 * repeat」を修正して、resultの値を"ABABABAB"
# 修正が不要であれば解答は「修正不要」とする。
"""
char1 = "A"
char2 = "B"
repeat = 4 & 7
result = char1 + char2 * repeat
print(result)  # 出力: "ABBBB"
"""



### 6. 数値演算と論理演算
## 問題
# 「result = A or not B」を修正して、resultの値をTrueにする
# 修正が不要であれば解答は「修正不要」とする。
"""
x = 7
y = 3
A = x % y
B = x > y
result = A or not B
print(result)
"""



### 7. ビット演算と数値操作
## 問題
# 「result = x << y & 3」を修正して、resultの値を4にする。
# 修正が不要であれば解答は「修正不要」とする。
"""
x = 2
y = 5
result = x << y & 3
print(result)  # 出力: 0
"""



## 問題
# 「result = a % b == 0 and a >> 2 < b」を修正して、resultの値をTrueにする
# 修正が不要であれば解答は「修正不要」とする。
"""
a = 30
b = 5
result = a % b == 0 and a >> 2 < b
print(result)  # 出力: False
"""



### 9. 文字列と数値の組み合わせ
## 問題
# 修正が不要であれば解答は「修正不要」とする。
# 「result = "Python" + str(version & 3)」を修正して、resultの値を"Python3.12"
"""
version = 3.12
result = "Python" + str(version & 3)
print(result)
"""



### 10. 総合問題（複数の演算子）
## 問題
# 修正して、resultの値をTrueにする
# 修正が不要であれば解答は「修正不要」とする。
"""
x = 10
y = 5
result = (x & y == 0) or not (x % y)
print(result)
"""


