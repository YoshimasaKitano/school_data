# list_sample5.py
"""
for文を使ってリストから要素を取り出す
"""
colors = ["red", "blue", "green", "yellow", "pink"]

# while文を使う
i = 0
while i < len(colors):
    print(colors[i])
    i += 1

# for文を使う
for i in range(len(colors)):
    print(colors[i])

# for文を使う2
for color in colors:
    print(color)

## カウンターをつけて表示する
for i,color in enumerate(colors):
    print(i,color)

for i in range(len(colors)):
    print(i,colors[i])

i = 0
while i < len(colors):
    print(i,colors[i])
    i += 1

## 複数のリストを対象にする
# name1とname2の要素を連結して空のリストに追加する
name1 = ["鈴木", "田中", "赤尾", "佐々木", "高田"]
name2 = ["星奈", "優美", "恵子", "薫花", "幸恵"]
longname = []

for n in zip(name1,name2):
    print(n)
    print(type(n)) ### <class 'tuple'>

for n1,n2 in zip(name1,name2):
    n = n1 + n2
    longname.append(n)

print(longname) ### ['鈴木星奈', '田中優美', '赤尾恵子', '佐々木薫花', '高田幸恵']

"""練習1
1~30のランダムな整数値を5つ要素にもつリストを作成する
ヒント：繰り返し乱数を生成してリストに追加する
"""

"""練習2
練習1のリストの要素を3倍した値を要素に持つリストを作成する
ヒント：練習1のリストから順に要素を取得し、3倍して新しいリストに追加する
"""

"""練習3
練習1と2で作成したリストのそれぞれの要素を合計した値を要素に持つリストを作成する
"""

# 練習1
from random import randint
nums = []
for i in range(5):
    num = randint(1,30)
    nums.append(num)
print(nums)
nums_copy = nums.copy()

# 練習2
num_3 = []
for i in range(len(nums)):
    num3 = nums.pop(0)
    num3 *= 3
    num_3.append(num3)
print(num_3)

# 練習3
num_total = []
for i, j in zip(nums_copy,num_3):
    num_total.append(i + j)

print(num_total)

## リスト内包表記
# nums = [0,1,2,3,4] リストを作る
nums = []
for i in range(5):
    nums.append(i)

print(nums) ### [0, 1, 2, 3, 4]

# リスト内包表示
nums = [i for i in range(5)]


print(nums) ### [0, 1, 2, 3, 4]

# 練習1(リスト内包表記)
from random import randint
nums = [randint(1,30) for i in range(5)]
print(nums)
nums_copy = nums.copy()

# 練習2(リスト内包表記)
num_3 = [num*3 for num in nums]
print(num_3)

# 練習3(リスト内包表記)
num_total = [i + j for i, j in zip(nums,num_3)]
print(num_total)
 
 ## 条件付きリスト内包表記
 # for文を使って1~30までの3の倍数を要素に持つリストを作成する
nums3 = []
for i in range(1,31):
    if i % 3 == 0:
        nums3.append(i)
    
print(nums3) ### [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

# リスト内包表記
nums3 = [i for i in range(1,31) if i % 3 == 0]
print(nums3) ### [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

## 条件が複数ある場合
# for文を使って1~30までの3の倍数の偶数を要素を持つリストを作成する
nums3 = []
for i in range(1,31):
    if i % 3 == 0: # 3の倍数を判断
        if i % 2 == 0: # 偶数を判断
            nums3.append(i)
    
print(nums3) ### [6, 12, 18, 24, 30]

# リスト内包表記
nums3 = [i for i in range(1,31) if i % 3 == 0 if i % 2 == 0]
print(nums3) ### [6, 12, 18, 24, 30]

## 多重リスト
apartment = [["佐藤", "田中", "山田"],["西山", "近藤", "青木"]]
print(apartment) ### [['佐藤', '田中', '山田'], ['西山', '近藤', '青木']]
print(apartment[0][0]) ### 佐藤
print(apartment[0][1]) ### 田中
print(apartment[0][2]) ### 山田

print(apartment[1][0]) ### 西山
print(apartment[1][1]) ### 近藤
print(apartment[1][2]) ### 青木

print("----------------------")
for i in range(2):
    print(str(i)+"階の住人")
    for j in range(3):
        print(apartment[i][j])

# リスト内包表記
lives_list = [apartment[i][j] for i in range(2) for j in range(3)]
print(lives_list) ### ['佐藤', '田中', '山田', '西山', '近藤', '青木']

## リスト内を検索する
# lives_list内に"山田"がいるか？を検索する
res = False
for name in lives_list:
    if name == "山田":
        res = True
        break 
print(res) ### True

# in演算子を使う
# 存在する場合Trueを返し、存在しない場合Falseを返す
print("山田" in lives_list) ### True
print("井上" in lives_list) ### False

# 存在する場合、インデックス番号を返す index()メソッド
print(lives_list.index("山田")) ### 2

try:
    print(lives_list.index("井上")) ### ValueError: '井上' is not in list
except ValueError:
    print("存在しません")

## リストの中に指定した値がいくつあるかを検索する
# 1~6の値を10個持つリストを作る
numbers = [randint(1,6) for i in range(10)]
print(numbers)

# 値がいくつあるかを検索count()メソッド
# 見つからない場合は0を返す
print(f"1の数：{numbers.count(1)}")
print(f"2の数：{numbers.count(2)}")
print(f"3の数：{numbers.count(3)}")
print(f"4の数：{numbers.count(4)}")
print(f"5の数：{numbers.count(5)}")
print(f"6の数：{numbers.count(6)}")

## リストからランダムに要素を取り出す
# randomモジュールのchoice()関数
import random
lives_list = ['佐藤', '田中', '山田', '西山', '近藤', '青木']

for i in range(5):
    name = random.choice(lives_list)
    print(i,name)

print(lives_list)

## リストの要素の合計値、最大値、最小値を取得する
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("合計値：",sum(nums))
print("最大値：",max(nums))
print("最小値：",min(nums))

# print(sum(lives_list)) ### TypeError: unsupported operand type(s) for +: 'int' and 'str'

"""練習
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
リストnumsからランダムに要素を5つ取得して新しいリストnums2をリスト内包表記で作成
nums2の要素の最大値、最小値、合計値を取得する
"""
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
nums2 = [random.choice(nums) for i in range(5)]
print(nums2)
print("最大値：",max(nums2))
print("最小値：",min(nums2))
print("合計値：",sum(nums2))

"""練習問題
キーボード入力で文字列を取得
規則的に文字増やす
[例]
文字列を入力→abcde
結果:abbcccddddeeeee
"""
# for
s = list(input("文字列を入力→"))
nums = []

for i in range(len(s)):
    num = s[i] * (i+1)
    nums.append(num)

print("".join(nums))

"""模範解答
"""
# while
s = input("文字列を入力→")

l = list(s)
l2 = []
i = 0
while i < len(l):
    l2.append(l[i] * (i + 1))
    i += 1

s2 = "".join(l2)
print(s2)

# 文字列操作
s = input("文字列を入力→")

s2 = ""
for i, char in enumerate(s):
    s2 += char * (i + 1)

print(s2)