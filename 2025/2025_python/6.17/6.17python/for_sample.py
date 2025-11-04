# for_sample.py
"""
for文 繰り返し処理
"""
# 文字列から1文字ずつ順番に取得する
text = "python"
for s in text:
    print(s)

print("終了")

# 指定回数だけ繰り返す
for i in range(5):
    print("python")

for i in range(5):
    print(i)

"""
range(開始値,終了値,ステップ値)
"""
for i in range(2,10,2):
    print(i)

"""練習
range()を使って
1,1~20までの奇数を表示する
2,1~20までの偶数を表示する
"""

for i in range(1,21,2):
    print(i,end = " ")

print()

for i in range(2,21,2):
    print(i,end = " ")

print()

"""
for文のネスト
"""
for i in range(3):
    print("i=",i)

    for j in range(2):
        print(" j=",j)

print("終了")

"""練習
＠＠＠＠＠
＠＠＠＠＠
＠＠＠＠＠
＠＠＠＠＠
＠＠＠＠＠
"""

for i in range(0,5):
    for j in range(5):
        print("＠",end = "")
    print()

# for i in range(0,1):
#     for j in range(1):
#         print("＠",end = "")
#     print()
# for i in range(1,2):
#     for j in range(2):
#         print("＠",end = "")
#     print()
# for i in range(2,3):
#     for j in range(3):
#         print("＠",end = "")
#     print()
# for i in range(3,4):
#     for j in range(4):
#         print("＠",end = "")
#     print()
# for i in range(4,5):
#     for j in range(5):
#         print("＠",end = "")
#     print()

for i in range(5):
    for j in range(i+1):
        print("＠",end = "")
    print()

for i in range(5):
    for j in range(5-i):
        print("＠",end = "")
    print()
