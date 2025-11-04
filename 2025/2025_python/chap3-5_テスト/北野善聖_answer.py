# 北野善聖_answer.py
"""
名前:
"""
## 問題１
print("=== 問題１ ===")
# ここから下にソースコードを記述する。
from random import randint
money = randint(1000,10000)
five = money // 500 
one = (money - five * 500 ) // 100
fifty = (money - (five * 500 + one * 100)) // 50
ten = (money - (five * 500 + one * 100 + fifty * 50)) // 10
five_only = (money - (five * 500 + one * 100 + fifty * 50 + ten * 10)) // 5
one_only = (money - (five * 500 + one * 100 + fifty * 50 + ten * 10 + five_only * 5)) / 1
one_only = int(one_only)
print(f"金額：{money}")
print(f"500円硬貨は{five}枚")
print(f"100円硬貨は{one}枚")
print(f"50円硬貨は{fifty}枚")
print(f"10円硬貨は{ten}枚")
print(f"5円硬貨は{five_only}枚")
print(f"1円硬貨は{one_only}枚")



print("プログラム終了")

## 問題２
print("=== 問題２ ===")
# ここから下にソースコードを記述する。
result = 0
count = 0
while count < 5:
    text = input("文字を入力：")
    if len(text) == 0:
        print("**入力エラー")
    else:
        result += len(text)
        count += 1
print(f"入力合計文字数は、{result}です。")




print("プログラム終了")

## 問題3
print("=== 問題３ ===")
# ここから下にソースコードを記述する。
from math import floor
h = 0
w = 0
h = float(input("身長(cm)を入力："))
w = float(input("体重(kg)を入力："))
h_m = h / 100
bmi = floor((w / (h_m * h_m)) * 100 )/100
if bmi < 18:
    body = "やせ型"
elif 18 <= bmi < 25:
    body = "標準型"
elif 25 <= bmi < 30:
    body = "肥満型"
elif bmi >= 30:
    body = "重度肥満型"
print(f"BMI値：{bmi}")
print(f"体型：{body}")


print("プログラム終了")

## 問題4
print("=== 問題４ ===")
# ここから下にソースコードを記述する。
count1 = 6
while count1 >= 1:
    count2 = 1
    if count1 == 6:
        print("6階[レストラン]")
        count1 -= 1
    if count1 == 1:
        print("1階[フロント/ロビー]")
    else:
        while count2 < 8:
            if count1 == 4 and count2 == 2:
                print("[S-S]", end = "")
            elif count1 == 4 and count2== 4:
                print("[S-S]", end = "")
            else:
                print(f"{count1}階[{count1}-{count2}]", end = "")
            count2 += 1
    count1 -= 1
    print()



print("プログラム終了")
