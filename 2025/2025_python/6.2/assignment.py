# assignment.py
"""
代入演算子
= 左辺に右辺を代入する

複合代入演算子
a += 1 は、a = a + 1と同じ処理
a -= 1 は、a = a - 1と同じ処理
a *= 2 は、a = a * 2と同じ処理
a /= 2 は、a = a / 2と同じ処理
a %= 2 は、a = a % 2と同じ処理
a **= 3 は、a = a ** 3と同じ処理

"""
age = 19
age += 1 # age = age + 1
print(age) ### 20

age -= 1
print(age) ### 19

age *= 2
print(age) ### 38

age /= 2
print(age) ### 19.0

age %= 2
print(age) ### 1.0

age **= 3
print(age) ### 1.0

# 文字列に使える複合代入演算子
# += 
who = "猫"
text = ""

text = "我が輩は"
print(text) ### 我が輩は
text += who # text = text + who
print(text) ### 我が輩は猫

text += "である。"
print(text) ### 我が輩は猫である。

text *= 3 # text = text * 3
print(text) ### 我が輩は猫である。我が輩は猫である。我が輩は猫である。

"""
text **= 2 ### TypeError:型に対するエラー
print(text)
"""
a = "A"
b = "B"

# 交換処理
t = a
print(a) ### A
a = b
print(a) ### B
b = t

print("変数a:",a) ### 変数a: B
print("変数b:",b) ### 変数b: A
