# janken.py
"""
じゃんけんのプログラム
<仕様>
・3回勝つか負けるかでゲーム終了
・ここまで学習した内容で作成する
    ※リストなどは使用禁止
    条件分岐、繰り返し処理、例外処理を使用する。
 ・対戦中や結果の表示はしっかり作りこんでください
"""
from random import randint
win = 0
lose = 0
even = 0
i = 1
text = "最初はグーじゃんけん、、、"
print("=================")
print("じゃんけんゲーーム")
print("=================")
while win < 3 and lose < 3:
    hand = input(f"{i}回戦目！{text}")
    enemy = randint(1,3)

    if enemy == 1:
        enemy = "グー"
    
    elif enemy == 2:
        enemy = "チョキ"

    elif enemy == 3:
        enemy = "パー"

    if hand == enemy:
        print("あいこ！")
        even += 1
        text = "あいこで、、、"
        
    elif enemy == "グー" and hand == "チョキ":
        print("私はグーを出しました！")
        print("グーVSチョキであなたの負け！")
        lose += 1
        text = "最初はグーじゃんけん、、、"

    elif enemy == "グー" and hand == "パー":
        print("私はグーを出しました！")
        print("グーVSパーであなたの勝ち！")
        win += 1
        text = "最初はグーじゃんけん、、、"

    elif enemy == "チョキ" and hand == "グー" :
        print("私はチョキを出しました！")
        print("チョキVSグーであなたの勝ち！")
        win += 1
        text = "最初はグーじゃんけん、、、"

    elif enemy == "チョキ" and hand == "パー":
        print("私はチョキを出しました！")
        print("チョキVSパーであなたの負け！")
        lose += 1
        text = "最初はグーじゃんけん、、、"

    elif enemy == "パー" and hand == "グー":
        print("私はパーを出しました！")
        print("パーVSグーであなたの負け！")
        lose += 1
        text = "最初はグーじゃんけん、、、"

    elif enemy == "パー" and hand == "チョキ":
        print("私はパーを出しました！")
        print("パーVSチョキであなたの勝ち！")
        win += 1
        text = "最初はグーじゃんけん、、、"
    else:
        print("グー、チョキ、パーのどれかを入力してね！")
        i -= 1
        text = "最初はグーじゃんけん、、、" 

    i += 1

if win == 3:
    i -= 1
    print(f"おめでとう！{i}回やって、3:{lose}、引き分け{even}であなたの勝ち！")

elif lose == 3:
    i -= 1
    print(f"残念。{i}回やって、{win}:3、引き分け{even}であなたの負け。また挑戦してね！")

# from random import randint
# win = 0
# lose = 0
# even = 0
# i = 1
# text = "最初はグーじゃんけん、、、"
# print("=================")
# print("じゃんけん連戦連勝ゲーム")
# print("=================")
# while lose < 1 and even < 1:
#     hand = input(f"{i}回戦目！{text}")
#     enemy = randint(1,3)

#     if enemy == 1:
#         enemy = "グー"
    
#     elif enemy == 2:
#         enemy = "チョキ"

#     elif enemy == 3:
#         enemy = "パー"

#     if hand == enemy:
#         print("あいこ！")
#         even += 1

#     elif enemy == "グー" and hand == "パー":
#         print("私はグーを出しました！")
#         print("グーVSパーであなたの勝ち！")
#         win += 1

#     elif enemy == "チョキ" and hand == "グー" :
#         print("私はチョキを出しました！")
#         print("チョキVSグーであなたの勝ち！")
#         win += 1

#     elif enemy == "チョキ" and hand == "パー":
#         print("私はチョキを出しました！")
#         print("チョキVSパーであなたの負け！")
#         lose += 1

#     elif enemy == "パー" and hand == "グー":
#         print("私はパーを出しました！")
#         print("パーVSグーであなたの負け！")
#         lose += 1

#     elif enemy == "パー" and hand == "チョキ":
#         print("私はパーを出しました！")
#         print("パーVSチョキであなたの勝ち！")
#         win += 1
#     else:
#         print("グー、チョキ、パーのどれかを入力してね！")
#         i -= 1

#     i += 1

# print(f"記録:{win}連勝達成")