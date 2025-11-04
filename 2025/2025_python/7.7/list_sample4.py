# list_sample4.py
"""
リストの要素を並び替える
"""
## ソート
numbers = [30, 50, 10, 40, 20]

# 基本選択法でソートする
i = 0
t = 0
while i < 4:
    j = i + 1
    while j < 5:
        if numbers[i] > numbers[j]:
            t = numbers[i]
            numbers[i] = numbers[j]
            numbers[j] = t

        j += 1
    i += 1

print(numbers)

"""模範解答
"""
i = 0
while i < len(numbers):
    j = i + 1 # jの始まりはiの隣
    while j < len(numbers):

        # 比較処理
        if numbers[i] > numbers[j]:
            # 交換処理
            t = numbers[i]
            numbers[i] = numbers[j]
            numbers[j] = t

        j += 1
    i += 1

print(numbers) ### [10, 20, 30, 40, 50]

# バブルソート
numbers = [30, 50, 10, 40, 20]
i = len(numbers)
while i > 1:
    j = 1
    while j < i:
        # 隣り合う要素を比較して交換する
        if numbers[j] < numbers[j-1]:
            t = numbers[j]
            numbers[j] = numbers[j-1]
            numbers[j-1] = t
            

        j += 1
    i -= 1

print(numbers) ### [10, 20, 30, 40, 50]

## 昇順にソートする sort()メソッド
numbers = [30, 50, 10, 40, 20]
numbers.sort()
print(numbers) ### [10, 20, 30, 40, 50]

## 降順にソートする sort(reverse=True)メソッド
numbers = [30, 50, 10, 40, 20]
numbers.sort(reverse=True)
print(numbers) ### [50, 40, 30, 20, 10]

## 文字列のリストのソート
# アルファベット順
str_list = ["c", "f", "b", "a", "d", "e"]
str_list.sort()
print(str_list) ### ['a', 'b', 'c', 'd', 'e', 'f']

# 日本語 ひらがな
str_list = ["か", "ま", "い", "た", "ち"]
str_list.sort(reverse=True)
print(str_list) ### ['ま', 'ち', 'た', 'か', 'い']

## ソートされたリストを作る sorted()関数
numbers = [30, 50, 10, 40, 20]

# 昇順にソートされたリストを作る
numbers2 = sorted(numbers)
print(numbers2) ### [10, 20, 30, 40, 50]
print(numbers) ### [30, 50, 10, 40, 20]

# 降順にソートされたリストを作る
numbers2 = sorted(numbers,reverse=True)
print(numbers2) ### [50, 40, 30, 20, 10]

## 逆順に並び替える
numbers = [30, 50, 10, 40, 20]

# スライス
numbers2 = numbers[::-1]
print(numbers2) ### [20, 40, 10, 50, 30]

# numbers自体を逆順に並び替える reverse()メソッド
numbers.reverse()
print(numbers) ### [20, 40, 10, 50, 30]

## リストの要素をランダムに並び替える
numbers = [10, 20, 30, 40, 50]

import random
random.shuffle(numbers)
print(numbers) ### [30, 20, 10, 50, 40]

str_list = ["a", "ab", "abc", "abcd", "abcde"]
random.shuffle(str_list)
print(str_list) ### ['abcd', 'abcde', 'ab', 'a', 'abc']

# 文字数順に並べる
str_list.sort(key=len)
print(str_list) ### ['a', 'ab', 'abc', 'abcd', 'abcde']

# 大文字、小文字の区別
str_list = ["a", "Ab", "ABc", "abCD", "abcDe"]
str_list2 = sorted(str_list)
print(str_list2) ### ['ABc', 'Ab', 'a', 'abCD', 'abcDe']

# 区別しない
str_list3 = sorted(str_list,key=str.lower)
print(str_list3) #　['a', 'Ab', 'ABc', 'abCD', 'abcDe']

"""練習
str_list = ["a", "b", "c", "d", "e"]
ランダムに抜き出して表示する
・random.choice()は使わないこと
"""
import random
str_list = ["a", "b", "c", "d", "e"]
while len(str_list) > 0:
    num = random.randint(0,len(str_list))
    print(str_list.pop(num-1))

print("終了！")

str_list = ["a", "b", "c", "d", "e"]
random.shuffle(str_list)
while len(str_list) > 0:
    print(str_list.pop())

print("終了！")