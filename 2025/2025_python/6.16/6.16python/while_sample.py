# while_sample.py
"""
while文 繰り返し処理
"""
# 1から5までカウントアップ表示する
count = 1

while count <= 5:
    print(count)

    count += 1 # count = count + 1

# 5から0までカウントダウン表示する
count = 5

while count >= 0:
    print(count)

    count -= 1

# 1~9の乱数を生成し、その値の回数だけPythonと表示する。

# カウンター変数なし
from gettext import find
from random import randint
num = randint(1,9)

while num > 0:
    print("Python")

    num -= 1

# カウンター変数あり
from random import randint
num = randint(1,9)
count = 0
while count < num:
    print("Python")
    count += 1

## 繰り返し中に条件が満たされた場合、繰り返しから抜ける処理
# break文
"""
a,b,cの3つの値の合計値が21になったらbreakする
"""
# while True: # 無限ループ

#     input("Enter")

#     a = randint(1,13)
#     b = randint(1,13)
#     c = randint(1,13)

#     if (a + b + c) == 21:
#         break

# print(a,b,c)

"""
3回間違えるか、qと入力されるまで出題を繰り返す
"""
# from random import randint
# miss = 0
# correct = 0

# print("問題！3回間違えたら終了。qで止める")

# while miss < 3:
#     a = randint(1,100)
#     b = randint(1,100)
#     ans = a + b

#     question = f"{a} + {b} は？"
#     value = input(question)

#     if value == "q":
#         break

#     if value == str(ans):
#         print("正解です！")
#         correct += 1
#     else:
#         miss += 1
#         print("間違い！","x" * miss)

# print("--------------")
# print("正解:",correct)
# print("間違い:",miss)

"""
continue文 スキップ処理
"""
# 1~30までカウントアップする
# 5の倍数だけスキップする
count = 0
while count < 30:

    count += 1

    # 5の倍数だけスキップする
    if count % 5 == 0:
        continue

    print(count)

"""
1~30まで数えて3の倍数と3のつく値の場合のだけ"Yes"と表示する
"""
# count = 0
# while count < 30:

#     count += 1

#     if count % 3 == 0 or "3" in str(count):
#         print("Yes")
#         continue

#     print(count)

# count = 0
# while count < 30:

#     count += 1

#     if count % 3 == 0 or "3" in str(count):
#         print("Yes")
        
#     else:
#         print(count)
count = 0
while count < 30:

    count += 1

    if count % 3 == 0 or str(count).find("3") != -1:
        print("Yes")
        continue

    print(count)

"""
while-else文
"""
# 0~9までカウントアップ
c = 0
while c < 10:

    if c == 3:
        c += 1
        continue

    print(c)
    c += 1

else:
    print("最後までカウントしました！")

print("終了")

"""
while文 文字の取得
"""
text = "python"

# print(text[0])
# print(text[1])
# print(text[2])
# print(text[3])
# print(text[4])
# print(text[5])

i = 0
while i < 6:
    print(text[i],end = " ") ### p y t h o n
    i += 1

"""練習
キーボードから文字列を取得して
1文字ずつ繰り返し順に表示する
"""

s = input("入力→")

i = 0
len_s = len(s)
while  i < len_s:
    print(s[i],end = " ")
    i += 1 
