# while文に関わる問題 10問
# 以下の乱数は各問題で使用します。変更しないでください。
from random import randint
numA = randint(0,20)
print("数値A:"+str(numA))

### レベルA（3問）
# Q1：1〜numAまで表示
""" 実行結果表示例
数値A:6
1 2 3 4 5 6
"""
i = 1
while i <= numA:
    print(i,end=" ")
    i += 1
print()



# Q2：numAの半分回「Hello」表示
""" 実行結果表示例
Hello
Hello
Hello
"""
i = 0
while i < numA // 2:
    print("Hello")
    i += 1


# Q3：0〜numAの偶数を表示
""" 実行結果表示例
0 2 4 6
"""
i = 0
while i < numA:
    if i % 2 == 0:
        print(i, end=" ")
    i += 1
print()

### レベルB
# Q4：合計が100を超えるまで0～9の乱数を加算
""" 実行結果表示例
合計: 108
"""
result = 0
while result < 100:
    result += randint(0, 9)
print(f"合計: {result}")


# Q5：繰返し0～9の乱数を加算、乱数が0または合計が50を超えたらbreakして終了する
""" 実行結果表示例
加算値:1 合計1
0が出ました！
プログラム終了！合計:1

加算値:6 合計6
加算値:2 合計8
加算値:7 合計15
加算値:8 合計23
加算値:3 合計26
加算値:9 合計35
加算値:4 合計39
加算値:9 合計48
加算値:3 合計51
50を超えました。
プログラム終了！合計:51
"""
result = 0
i = 1
while i != 0 or result < 50:
    i = randint(0, 9)
    if i != 0:
        result += i
        print(f"加算値:{i} 合計{result}")
    else:
        print("0がでました！")
        break
if result > 50:
    print("50を超えました。")
print(f"プログラム終了！合計:{result}")



# Q6：繰返し文字列を入力、「exit」で終了
""" 実行結果表示例
文字列入力→
入力: 
文字列入力→a
入力: a
文字列入力→exit
プログラム終了
"""
while True:
    text = input("文字列入力→")
    if text == "exit":
        print("プログラム終了")
        break
    else:
        continue



# Q7：0～9の乱数の奇数だけを10回合計する
""" 実行結果表示例
5 1 3 3 9 5 7 5 9 1
奇数合計: 48
"""
result = 0
count = 1
while count < 11:
    i = randint(0, 9)
    if i % 2 != 0:
        print(i, end=" ")
        result += i
        count += 1
print()
print(f"奇数合計: {result}")



### 高レベル
# Q8：桁数カウント（0の場合は1桁）ー記号や先頭が０の場合も対応させる
# len()は✖、ー記号がある場合や先頭が０の場合も含まれるため使えない
""" 実行結果表示例
数値を入力→01234
桁数: 4
"""
i = 0
num = int(input("数値を入力→"))
if num == 0:
    i = 1
num_abs = abs(num)
while num_abs > 0:
    num_abs //= 10
    i += 1
print(f"桁数: {i}")





# Q9：三角形型の図形を描く
""" 実行結果表示例
*********
 *******
  *****
   ***
    *
"""
i = 1
j = 1
while i < 6:
    k = 1
    while k < i:
        print(" ", end = "")
        k += 1
    j = 1 + (2 * i)
    while j < 12:
        print("*", end = "")
        j += 1
    print()
    i += 1
# Q10：顔を描く
""" 実行結果表示例
----------
|●   ●   |
|        |
|  │     |
|        |
| ―――――  |
----------
"""
i = 1
while i < 8:
    j = 1
    while j < 11:
        if i == 1 or i == 7:
            print("-", end="")
        elif (2 <= i <= 6 and j == 1) or (2 <= i <= 6 and j == 10) or (i == 4 and j == 4):
            print("|", end="")
        elif (i == 2 and j == 2) or (i == 2 and j == 6):
            print("●", end="")
        elif i == 6 and 3 <= j <= 7:
            print("―", end="")
        else:
            print(" ", end="")
        j += 1
    print()
    i += 1

# i = 1
# while i < 2:
#     j = 1
#     while j < 11:
#         print("-", end="")
#         j += 1
#     print()
#     i += 1
# i = 1
# while i < 2:
#     print("|", end="")
#     j = 1
#     while j < 9:
#         if j == 1 or j == 5:
#             print("●", end="")
#         else:
#             print(" ", end="")
#         j += 1
#     print("|")
#     i += 1
# i = 1
# while i < 2:
#     print("|", end="")
#     j = 1
#     while j < 9:
#         print(" ", end="")
#         j += 1
#     print("|")
#     i += 1
# i = 1
# while i < 2:
#     print("|", end="")
#     j = 1
#     while j < 9:
#         if j == 3:
#             print("|", end="")
#         else:
#             print(" ", end="")
#         j += 1
#     print("|")
#     i += 1
# i = 1
# while i < 2:
#     print("|", end="")
#     j = 1
#     while j < 9:
#         print(" ", end="")
#         j += 1
#     print("|")
#     i += 1
# i = 1
# while i < 2:
#     print("|", end="")
#     j = 1
#     while j < 9:
#         if 2 <= j <= 6:
#             print("―", end="")
#         else:
#             print(" ", end="")
#         j += 1
#     print("|")
#     i += 1
# i = 1
# while i < 2:
#     j = 1
#     while j < 11:
#         print("-", end="")
#         j += 1
#     print()
#     i += 1
# i = 1


