# for_practice.py
""" 数字あてゲーム
forのネスト、break文、continue文の練習問題
<仕様>
・プレーヤーは3回までチャンスがある
・毎回1~9までの数字を入力
・答えが偶数ならcontinue、奇数で正解ならbreak
・正解できない場合「ゲームオーバー」と表示
"""
from random import randint
# 正解の数字
ans = randint(1,9)

for i in range(1,4):
    print(f"{i}回目のチャレンジ")
    num = int(input("1~9の数字を入力してください！"))
    if num % 2 == 0:
        print("偶数はスキップされます。")
        continue

    for j in range(1,10):
        if num == ans:
            print("正解、おめでとう")
            break
    else:
        print("残念")

    if num == ans:
        break
else:
    print(f"ゲームオーバー、正解は{ans}でした！")

