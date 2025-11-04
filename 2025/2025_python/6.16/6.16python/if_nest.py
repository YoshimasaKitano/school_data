# if_nest.py
"""
if文のネスト(入れ子)
"""
from random import randint
size = randint(5,20) # 5～20の乱数
weight = randint(20,40) # 20～40の乱数

result = ""

if size >= 10: # sizeの判定

    if weight >= 25: # weightの判定
        result = "合格"
    else:
        result = "不合格"

else:
    result = "不合格"

# 結果の表示
text = f"サイズ:{size}、重量:{weight}、結果:{result}"
print(text)

"""
論理演算子
"""
result2 = ""
if (size >= 10) and (weight >= 25): # sizeとweight判定
    result2 = "合格"
else:
    result2 = "不合格"

text = f"サイズ:{size}、重量:{weight}、結果:{result2}"
print(text)

"""練習
0～99の乱数を生成
・乱数が0の場合、「0です。」と表示
・乱数が偶数の場合で50より小さい場合
    「偶数で50より小さい」と表示
・乱数が偶数の場合で50以上の場合
    「偶数で50以上」と表示
・乱数が奇数の場合で50より小さい場合
    「奇数で50より小さい」と表示
・乱数が奇数の場合で50以上の場合
    「奇数で50以上」と表示

※if文のネストで作成
"""
num = randint(0,99)
result = ""

if num != 0:
    if num % 2 == 0:
        if num < 50:
            result = "偶数で50より小さい"
        elif num >= 50:
            result = "偶数で50以上"
    if num % 2 == 1:
        if num < 50:
            result = "奇数で50より小さい"
        elif num >= 50:
            result = "奇数で50以上"
else:
    result = "0です。"

text = f"数字:{num}、結果:{result}"
print(text)

"""
論理演算子
"""
num = randint(0,99)
result2 = ""

if num != 0:
    if (num % 2 == 0) and (num < 50):
        result2 = "偶数で50より小さい"
    elif (num % 2 == 0) and (num >= 50):
        result2 = "偶数で50以上"
    elif (num % 2 == 1) and (num < 50):
        result2 = "奇数で50より小さい"
    elif (num % 2 == 1) and (num >= 50):
        result2 = "奇数で50以上"
else:
    result2 = "0です。"

text = f"数字:{num}、結果:{result2}"
print(text)


if False:
    print("A")
else:
    print("B")

num = randint(0,9)
print(num)

if num % 2:
    print("奇数") # 余りが0の時はFalseになって実行されないのでif文は奇数の時だけ実行される
else:
    print("偶数")

# if-else文を1行で書く
res = "奇数" if num % 2 else "偶数"
print(res)

# 範囲指定
if num >= 0 and  (num < 5):
    print("0以上、5より小さい")
elif (num >= 5) and (num < 10):
    print("5以上、10より小さい")

# andを使わずに範囲指定する
if 0 <= num < 5:
    print("0以上、5より小さい")
elif 5 <= num < 10:
    print("5以上、10より小さい")