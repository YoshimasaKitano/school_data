### gene_sample.py
## ジェネレーター関数
from re import X


def menu_gen():
    yield "ワイン"
    yield "サラダ"
    yield "スープ"
    yield "ステーキ"
    yield "アイスクリーム"

menu = menu_gen()
print(type(menu)) ### <class 'generator'>

print(next(menu)) ### ワイン
print(next(menu)) ### サラダ
print(next(menu)) ### スープ
print(next(menu)) ### ステーキ
print(next(menu)) ### アイスクリーム

# print(next(menu)) ### StopIteration:

menu = menu_gen()
for item in menu:
    print(item)
"""
ワイン
サラダ
スープ
ステーキ
アイスクリーム
"""

## 数列の値を生成するジェネレータ
# ジェネレータ関数の定義
def num_generator():
    n = 0
    while True:
        num = n * n + 2 * n + 3
        yield num
        n += 1

# 何かを行う関数
def do_something(num):
    return (num % 2, num % 3)

# ジェネレータが返す値を使って処理を行う
gen = num_generator()
for i in range(1, 10):
    num = next(gen)
    result = do_something(num)
    print(result)

"""
(1, 0)
(0, 0)
(1, 2)
(0, 0)
(1, 0)
(0, 2)
(1, 0)
(0, 0)
(1, 2)
"""

## FizzBuzzゲーム
# FizzBuzzのジェネレータ関数の定義
def fizzbuzz():
    n = 1
    while True:
        if n % 15 == 0: # 3と5の倍数
            yield "FizzBuzz"

        elif n % 3 == 0: # 3nの倍数
            yield "Fizz"

        elif n % 5 == 0: # 5の倍数
            yield "Buzz"

        else: # どれでもない場合
            yield str(n)

        n += 1

# fizzbuzz()でgameジェネレータを作って20回呼び出す
game = fizzbuzz()
for i in range(1, 20):
    print(next(game))

"""
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
"""

# def word_quiz(word):
#     hint = ""
#     for letter in word:
#         hint += letter
#         yield hint

# # 出題する
# ans = "Python"
# quiz = word_quiz(ans)
# while True:
#     try:
#         hint = next(quiz)
#         print(hint)
#         word = input("この単語は？:")
#         if ans.lower() == word.lower():
#             point = len(ans) - len(hint)
#             print(f"正解です！得点：{point}")
#             break
#         else:
#             print("違います。")
#     except Exception as e:
#         print("終了 得点：0")
#         print(e)
#         break

"""
P
この単語は？:Python
正解です！得点：5
"""

# ジェネレータ式でジェネレータを生成
odd_gen = (odd for odd in range(1, 6, 2)) # 丸かっこで囲む
print(type(odd_gen)) ### <class 'generator'>

# ジェネレータから値を表示
for num in odd_gen:
    print(num)

"""
1
3
5
"""

# ジェネレータからリストを作る
odd_gen = (odd for odd in range(1, 6, 2))
list_data = list(odd_gen) # list()でリスト化する

print(type(list_data)) ### <class 'list'>
print(list_data) ### [1, 3, 5]


# ジェネレータに値を送る
def testgen():
    n = 0
    while True:
        received = yield n # 値を受け取る
        if received:
            n = received
        else:
            n += 1

gen = testgen()

next(gen) # 初期化処理に使う
# print(next(gen)) ### 0
# print(next(gen)) ### 1

print(gen.send(10)) ### 10 # send()でyieldに値を送る
print(next(gen)) ### 11
print(next(gen)) ### 12

## サブジェネレータ
# ジェネレータの中に別のジェネレータを呼び出す
# yield from 構文で呼び出す
# サブジェネレータを定義
def sub_gen():
    yield "A"
    yield "B"

# メインジェネレータを定義
def main_gen():
    yield "start"
    yield from sub_gen() # サブジェネレータを呼び出す
    yield from range(0, 3) # range()関数から呼び出す
    yield from [10, 20, 30] # リストから呼び出す
    yield from "abc" # 文字列から呼び出す
    yield "end"

# main_gen()ジェネレータを生成
gen = main_gen()

for item in gen:
    print(item)
"""
start
A
B
0
1
2
10
20
30
a
b
c
end
""" 

## 値の合計を返すサブジェネレータ
def sub_gen():
    total = 0
    while True:
        x = yield
        
        if x is None:
            break
        total += x

    return total

def main_gen():
    result = yield from sub_gen()
    print(f"合計:{result}")

gen = main_gen()
next(gen)
try:
    gen.send(3)
    gen.send(5)
    gen.send(None)
except StopIteration as e:
    print("終了")
    print(e)