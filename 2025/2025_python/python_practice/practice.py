# 3回間違えたら失敗。qと入力されたら終わる。

# from random import randint
# miss = 0
# ans = 0

# while miss < 3:
#     numA = randint(1,100)
#     numB = randint(1,100)
#     result = numA + numB
#     text = input(f"{numA}+{numB}=")
#     if text == "q":
#         break
#     try:
#         text = int(text)

#         if text == result:
#             print("正解！やりますねぇ")
#             ans += 1

#         elif text != result:
#             print("残念！もっと勉強してね！")
#             miss += 1

#     except ValueError as text:
#         print("数字を入力してね！")
#         continue

# print(f"{ans}回連続正解！")


# 九九の表
# for i in range(1,10):
#     for j in range(1,10):
#         print(i * j, end=" ")
#     print()

# じゃんけん
# from random import randint
# win = 0
# lose = 0
# while win < 3 and lose < 3:
#     enemy = randint(1,3)
#     try:
#         me = int(input("1～3の数字を入力してください。1:グー 2:チョキ 3:パー"))
#     except:
#         print("1~3の数字を入力してください")
#         continue
#     if me > 3 or me < 1:
#         print("1~3の数字を入力してください")
#         continue
#     if me == enemy:
#         print("あいこ！")
#         continue
#     elif enemy == 1 and me == 2:
#         print("あなたのまけ")
#         lose += 1
#     elif enemy == 1 and me == 3:
#         print("あなたのかち")
#         win += 1
#     elif enemy == 2 and me == 1:
#         print("あなたのかち")
#         win += 1
#     elif enemy == 2 and me == 3:
#         print("あなたのまけ")
#         lose += 1
#     elif enemy == 3 and me == 1:
#         print("あなたのまけ")
#         lose += 1
#     elif enemy == 3 and me == 2:
#         print("あなたのかち")
#         win += 1

# if win == 3:
#     result = "かち！"
# elif lose == 3:
#     result = "まけ！"

# print(f"勝ち：{win} 負け：{lose}であなたの{result}")

# 図形
# for i in range(1,6):
#     for j in range(1,i+1):
#         print("＠",end="")
#     print()

# for i in range(1,6):
#     for j in range(1,7-i):
#         print("＠",end="")
#     print()

# ビンゴゲーム
# from random import randint
# num = randint(1,5)
# input("Enterキーを押してください")
# if num == 1:
#     print("りんご")
# elif num == 2:
#     print("みかん")
# elif num == 3:
#     print("ぶどう")
# elif num == 4:
#     print("いちご"fro
# elif num == 5:
#     print("はっさく")

# BMI
# from math import floor
# w = 0
# h = 0
# w = float(input("体重をkg単位で数字で入力してください"))
# h = int(input("身長をcm単位で数字で入力してください"))
# h /= 100
# bmi = w / (h * h)
# bmi = floor(bmi * 10) /10
# print(bmi)

# 九九
# for i in range(1,10):
#     for j in range(1,10):
#         print(i * j, end=" ")
#     print()

# 図形
# for i in range(1,6):
#     for j in range(1,i+1):
#         print("＠",end="")
#     print()

# for i in range(1,6):
#     for j in range(1,7-i):
#         print("＠",end="")
#     print()

# for i in range(1,6):
#     for j in range(1,6):
#         print("＠",end="")
#     print()

# じゃんけん
from random import randint
win = 0
lose = 0
while win < 3 and lose < 3:
    enemy = randint(1,3)
    me = input("1~3で数字を入力してください。1：グー、2：チョキ、3：パー")
    if me == "q":
        break
    try:
        me = int(me)
    except:
        print("1~3の数字で入力してください")
        continue
    if enemy == me:
        print("あいこ")
        continue
    elif me < 1 or me > 3:
        print("1~3の数字で入力してください")
    elif enemy == 1 and me == 2:
        print("グーVSチョキであなたの負け")
        lose += 1
    elif enemy == 1 and me == 3:
        print("グーVSパーであなたの勝ち")
        win += 1
    elif enemy == 2 and me == 1:
        print("チョキVSグーであなたの勝ち")
        win += 1
    elif enemy == 2 and me == 3:
        print("チョキVSパーであなたの負け")
        lose += 1
    elif enemy == 3 and me == 1:
        print("パーVSグーであなたの負け")
        lose += 1
    elif enemy == 3 and me == 2:
        print("パーVSチョキであなたの勝ち")
        win += 1
if win == 3:
    result = "勝ち"
    print(f"勝ち：{win} 負け：{lose}であなたの{result}")
elif lose == 3:
    result = "負け"
    print(f"勝ち：{win} 負け：{lose}であなたの{result}")
elif me == "q":
    print("試合が中断されました")


