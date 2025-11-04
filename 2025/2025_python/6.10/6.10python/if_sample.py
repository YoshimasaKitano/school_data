# if_sample.py
"""
if文 条件分岐構造
"""
# サイコロ
from os import DirEntry
import random 
dice = random.randint(1,6)
print(dice)

## if文
# もし、diceが3以下の場合は、"サイコロは3以下"と表示する
if dice <= 3:
    print("サイコロは3以下")

## if-else文
if (dice <= 3):
    print("サイコロは3以下")
else:
    print("サイコロは3より大きい")

## if-elif-else文
if (dice <= 2):
    print("サイコロは1または2")
elif (dice <= 4):
    print("サイコロは3または4")
else:
    print("サイコロは5または6")

# 論理演算子を使う
if (dice == 1 or dice == 2):
    print("サイコロは1または2")

if (dice == 3 or dice == 4):
    print("サイコロは3または4")

if (dice == 5 or dice == 6):
    print("サイコロは5または6")

""" 練習問題
0～100までの整数の乱数を生成
乱数が80以上の場合、"Aクラス"と表示
乱数が60以上の場合、"Bクラス"と表示
乱数が40以上の場合、"Cクラス"と表示
乱数が40より小さい場合、"落第"と表示
"""

import random

name = input("名前を入力してください")

num = random.randint(0,100)

result = 0
if num >= 80:
    result ="Aクラス"
elif num >= 60:
    result = "Bクラス"
elif num >= 40:
    result = "Cクラス"
else:
    result = "落第"

# print(name + "さん" + str(num) + "点" + result)
print(f"{name}さん、{num}点:{result}")