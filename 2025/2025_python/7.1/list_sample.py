# list_sample.py
"""
リスト 複数の値を1つの値で扱う
"""
numbers = [4, 8, 15, 16, 23, 42]
print(numbers) ### [4, 8, 15, 16, 23, 42]

colors = ["red", "green", "blue"]
print(colors) ### ['red', 'green', 'blue']

mixture = [20, 30,
            "dog", "cat",
                True, False]
print(mixture) ### [20, 30, 'dog', 'cat', True, False]

print(type(mixture)) ### <class 'list'>

colors2 = colors * 2
print(colors2) ### ['red', 'green', 'blue', 'red', 'green', 'blue']

## 文字列をリストにする
list_python = list("python")
print(list_python) ### ['p', 'y', 't', 'h', 'o', 'n']

## range()を使ってリストを作る list()
number_list = list(range(5))
print(number_list) ### [0, 1, 2, 3, 4]

number_list2 = list(range(1,5))
print(number_list2) ### [1, 2, 3, 4]

number_list3 = list(range(1,10,2))
print(number_list3) ### [1, 3, 5, 7, 9]

## 要素が1つのリスト
list1 = ["a"]
print(list1) ### ['a']

## 要素が0個のリスト
list0 = []
print(list0) ### []
print(type(list0)) ### <class 'list'>

list0_2 = list()
print(list0_2) ### []

"""
リストの要素
"""
colors = ["blue", "red", "green", "yellow"]
print(colors[0]) ### blue
print(colors[1]) ### red
print(colors[-1]) ### yellow

# 文字列の要素は更新できない
str = "python"
print(str[2]) ### t
# str[2] = "x" ### 文字列の要素は更新できない
print(str)

# リストは要素が更新できる
colors[2] = "black"
print(colors) ### ['blue', 'red', 'black', 'yellow']

# リスト外の指定
# print(colors[4]) ### IndexError: list index out of range

# リストの要素の数を調べる
print(len(colors)) ### 4 要素が4つ入ったリストであることがわかる

"""
インデックス番号を入力して要素を取り出す
"""
colors = ["blue", "red", "green", "yellow"]
try:
    num = int(input("取り出す位置:"))
    print(colors[num])
except IndexError:
    print("インデックスエラー")

except ValueError:
    print("数値以外の入力がありました。")

except Exception as e: # その他のエラー時に内容を表示する
    print("エラー:" + e)
