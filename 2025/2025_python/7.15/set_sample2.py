# set_sample2.py
"""
セットの要素の追加、削除
"""
fruits = set() # 空のセットを作る
print(fruits) ### set()

# 要素の追加 add()メソッド
fruits.add("apple")
print(fruits) ### {'apple'}
fruits.add("orange")
print(fruits) ### {'apple', 'orange'}

## 重複する値は追加できない
fruits.add("orange")
print(fruits) ### {'orange', 'apple'}


fruits.add("banana")
fruits.add("peach")
print(fruits) ### {'peach', 'orange', 'apple', 'banana'}

# 要素の削除 remove()メソッド
fruits.remove("banana")
print(fruits) ### {'peach', 'orange', 'apple'}

# 指定した要素がない場合
# fruits.remove("banana") ### KeyError: 'banana'
print(fruits) ### {'peach', 'apple', 'orange'}

# 要素の削除 discard()メソッド
fruits.discard("peach")
print(fruits) ### {'orange', 'apple'}

# 指定した要素がない場合
fruits.discard("peach") ### なにもしない
print(fruits) ### {'orange', 'apple'}

# 要素を抜き取る pop()メソッド
## セットには末尾の要素がないため、何が抜き取られるかわからない
item = fruits.pop()
print(item) ### apple
print(fruits) ### {'orange'}

# セットを空にする clear()メソッド
fruits.clear()
print(fruits) ### set()

# セット自体を破棄する
del fruits
# print(fruits) ### NameError: name 'fruits' is not defined

"""
frozenset型
要素の追加、削除ができないセット
"""
# frozensetを作る frozenset()関数
data = frozenset("python")
print(data) ### frozenset({'y', 't', 'o', 'p', 'n', 'h'})

"""練習問題
1から9までの整数の乱数を要素に5つ持つセットを生成する
"""
from random import randint
nums = set()
i = 0
while i < 5:
    nums_copy = nums.copy()
    num = randint(1,9)
    nums.add(num)
    if len(nums) > len(nums_copy):
        i += 1
    else:
        continue
print(nums)

"""模範解答
"""
from random import randint

num_set = set() # 空のセットを用意
while len(num_set) < 5:
    num_set.add(randint(1,9))

print(num_set)

"""
セット内包表記
"""
# 1~5の整数を要素に持つセットを作る
num_set = {i for i in range(1,6)}
print(num_set) ### {1, 2, 3, 4, 5}

# 1~20までの奇数だけを要素に持つセットを作る
odd_set = set()
for i in range(1,21):
    if i % 2 != 0:
        odd_set.add(i)

print(odd_set) ### {1, 3, 5, 7, 9, 11, 13, 15, 17, 19}

# 1~20までの奇数だけを要素に持つセットをセット内包表記で作る
odd_set = {i for i in range(1,21) if i % 2 != 0}
print(odd_set) ### {1, 3, 5, 7, 9, 11, 13, 15, 17, 19}