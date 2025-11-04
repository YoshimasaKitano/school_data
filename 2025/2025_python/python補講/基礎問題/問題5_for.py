# for文に関わる問題 10問
# 以下の乱数は各問題で使用します。変更しないでください。
from random import randint
numA = randint(0,20)
print("数値A:"+str(numA))

### レベルA
# Q1：1〜nunAまで表示
""" 実行結果表示例
数値A:21
1 2 3 4 5 6
"""
for i in range(1, numA + 1):
    print(i, end=" ")
print()

# Q2：numAの半分回「Hello」表示
""" 実行結果表示例
Hello
Hello
Hello
"""
for i in range(numA // 2):
    print("Hello")

# Q3：0〜numAの偶数を表示
""" 実行結果表示例
0 2 4 6
"""
for i in range(numA + 1):
    if i % 2 == 0:
        print(i, end=" ")
print()

### レベルB
# Q4：0〜9の乱数を5回加算して合計を表示
""" 実行結果表示例
1回目: 9 → 合計: 9
2回目: 1 → 合計: 10
3回目: 2 → 合計: 12
4回目: 4 → 合計: 16
5回目: 9 → 合計: 25
最終合計: 25
"""
ans = 0
for i in range(1, 6):
    num = randint(0, 9)
    ans += num
    print(f"{i}回目: {num} → 合計:{ans}")
print(f"最終合計: {ans}")



# Q5：10個の乱数（0〜9）を生成し、偶数のみ合計する
""" 実行結果表示例
奇数: 3（スキップ）
偶数: 4 → 合計: 4
偶数: 6 → 合計: 10
偶数: 8 → 合計: 18
偶数: 0 → 合計: 18
奇数: 5（スキップ）
奇数: 3（スキップ）
偶数: 8 → 合計: 26
偶数: 4 → 合計: 30
奇数: 5（スキップ）
偶数合計: 30
"""
ans = 0
for i in range(10):
    num = randint(0, 9)
    if num % 2 != 0:
        print(f"奇数: {num}(スキップ)")
    else:
        ans += num
        print(f"偶数: {num} → 合計:{ans}")
print(f"偶数合計: {ans}")

# Q6：5回キーボードから文字列を入力し、入力の長さを表示
""" 実行結果表示例
1つ目の文字列→ a
「a」は 1 文字です
2つ目の文字列→ ab
「ab」は 2 文字です
3つ目の文字列→ abc
「abc」は 3 文字です
4つ目の文字列→ abcd
「abcd」は 4 文字です
5つ目の文字列→ abcde
「abcde」は 5 文字です
入力完了！
"""
for i in range(1, 6):
    text = input(f"{i}つ目の文字列→")
    ans = len(text)
    print(f"「{text}」は {ans} 文字です")
print("入力完了！")


# Q7：10個の乱数（1〜99）を生成して、最大・最小・平均を求める
""" 実行結果表示例
1回目: 14
2回目: 65
3回目: 76
4回目: 92
5回目: 55
6回目: 86
7回目: 80
8回目: 69
9回目: 14
10回目: 97
最大値: 97
最小値: 14
平均値: 64.8
"""
max = 0
min = 0
ans = 0
for i in range(1, 11):
    num = randint(1, 99)
    print(f"{i}回目: {num}")
    if min == 0 and max == 0:
        min = num
        max = num
    else:
        if num > max:
            max = num
        if num < min:
            min = num
    ans += num
average = ans / i
print(f"最大値: {max}")
print(f"最小値: {min}")
print(f"平均値: {average}")

### レベルC
# Q8：桁数カウント（0の場合は1桁））ー記号や先頭が０の場合も対応させる
# len()は✖、ー記号がある場合や先頭が０の場合も含まれるため使えない
""" 実行結果表示例
数値を入力→01234
桁数: 4
"""
count = 0
num = int(input("数値を入力→"))
if num == 1:
    count += 1
num_abs = abs(num)
for i, j in enumerate(str(num_abs)):
    count += 1
print(f"桁数: {count}")
    


# Q9：三角形型の図形を描く
""" 実行結果表示例
*********
 *******
  *****
   ***
    *
"""
for i in range(1, 6):
    for k in range(0, i):
        print(" ", end="")
    for j in range(1 + (2 * i), 12):
        print("*", end="")
    print()


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
for i in range(1, 8):
    for j in range(1, 11):
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
    print()
