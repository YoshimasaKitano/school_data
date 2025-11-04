# bmi.py
"""
身長(cm)と体重(kg)を入力してBMI値を表示する

#計算式
BMI値 = 体重(kg) / (身長(m) * 身長(m))

[実行イメージ]
身長(cm)の入力→170
体重(kg)の入力→60
結果BMI値:21.14

[仕様]
BMI値は小数点第2位以下切り捨て
身長の入力値は整数値
体重の入力値は浮動小数点

"""
from math import floor

shintyou = int(input("身長を入力してください→"))
taizyuu = float(input("体重を入力してください→"))
bmi = floor(taizyuu / (shintyou ** 2 / 10000) * 100) /100
print("BMI値:" + str(bmi))

"""
import math

# 身長(cm)と体重(kg)の入力処理
h = input("身長(cm)の入力→")
w = input("体重(kg)の入力→")

# 文字列型から数値型に変換
h = int(h)
w = float(w)

# BMIの計算
## BMI値 = 体重(kg) / (身長(m) * 身長(m))

h_m = h / 100 # cm → m に変換
bmi = w / (h_m * h_m)

# BMI値は小数点第2位以下切り捨て
math.floor(bmi * 100) /100

print("結果 BMI値:" + str(bmi))
"""
