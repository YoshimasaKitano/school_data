# dict_sample2.py
"""
辞書から値を取り出す
"""
data = {"red":3, "yellow":5, "blue":6, "green":2}
print(data["blue"]) ### 6s
# print(data["black"]) ### KeyError: 'black's
# エラーを回避する
try:
    print(data["black"])
except:
    print("データがありません。")

# キーがあれば値を返す、なければNoneを返す get()メソッド
print(data.get("blue")) ### 6
print(data.get("black")) ### None

# キーが存在するかを調べる
print("blue" in data) ### True
print("black" in data) ### False

# キーを取り出す
dict_data = {"red":3, "yellow":5, "blue":6, "green":2}

for key in dict_data:
    print(key) 
"""
red
yellow
blue
green
"""
## キーを使って値を取り出す
for key in dict_data:
    print(key, dict_data[key])
"""
red 3
yellow 5
blue 6
green 2
"""

## 辞書からキーを取り出してリストを作る
dict_data = {"red":3, "yellow":5, "blue":6, "green":2}

key_list = []
for key in dict_data:
    key_list.append(key)

print(key_list) ### ['red', 'yellow', 'blue', 'green']

## keys()メソッド
keys_obj = dict_data.keys()
print(keys_obj) ### dict_keys(['red', 'yellow', 'blue', 'green'])
print(type(keys_obj)) ### <class 'dict_keys'>

key_list = list(keys_obj)
print(key_list) ### ['red', 'yellow', 'blue', 'green']

## 短縮型
key_list = list(dict_data.keys())
print(key_list) ### ['red', 'yellow', 'blue', 'green']

for key in dict_data.keys():
    print(key)
"""
red
yellow
blue
green
"""

# 辞書から値を取り出してリストにする
dict_data = {"red":3, "yellow":5, "blue":6, "green":2}

value_list = []
for key in dict_data:
    value_list.append(dict_data[key])
print(value_list) ### [3, 5, 6, 2]

## values()メソッド
print(dict_data.values()) ### dict_values([3, 5, 6, 2])
print(type(dict_data.values())) ### <class 'dict_values'>

value_list = list(dict_data.values())
print(value_list) ### [3, 5, 6, 2]

for value in dict_data.values():
    print(value)
"""
3
5
6
2
"""

# 要素(キーと価)を取り出してリストにする
dict_data = {"red":3, "yellow":5, "blue":6, "green":2}

list_data = []
for key in dict_data:
    list_data.append((key, dict_data[key]))

print(list_data) ### [('red', 3), ('yellow', 5), ('blue', 6), ('green', 2)]

for t in list_data:
    print(t)
"""
('red', 3)
('yellow', 5)
('blue', 6)
('green', 2)
"""

for t in list_data:
    print(t[0], t[1])
"""
red 3
yellow 5
blue 6
green 2
"""

## items()メソッド
dict_data = {"red":3, "yellow":5, "blue":6, "green":2}

for key, value in dict_data.items():
    print(key, value)
"""
red 3
yellow 5
blue 6
green 2
"""

list_data = [(key, value) for key, value in dict_data.items()]
print(list_data) ### [('red', 3), ('yellow', 5), ('blue', 6), ('green', 2)]

print(dict_data) ### {'red': 3, 'yellow': 5, 'blue': 6, 'green': 2}

# 要素を抜き取って削除する
## pop()メソッド
dict_data = {"red":3, "yellow":5, "blue":6, "green":2}
# dict_data.pop() ### TypeError: pop expected at least 1 argument, got 0
# print(dict_data)

value = dict_data.pop("red") # pop()メソッドにキーを指定する
print(value) ### 3
print(dict_data) ### {'yellow': 5, 'blue': 6, 'green': 2}

## popitem()メソッド
dict_data = {"red":3, "yellow":5, "blue":6, "green":2}

item = dict_data.popitem() # 辞書から要素が何か抜き取られる
print(item) ## ('green', 2)
print(type(item)) ### <class 'tuple'>
print(dict_data) ### {'red': 3, 'yellow': 5, 'blue': 6}

for i in range(len(dict_data)):
    print(dict_data.popitem())
"""
('blue', 6)
('yellow', 5)
('red', 3)
"""
print(dict_data) ### {}

# dict_data.popitem() ### KeyError: 'popitem(): dictionary is empty'

fruit = {"apple":7, "orange":5, "peach":6}
while fruit: # fruitが空でなければ繰り返す
    key = input("どのフルーツを取り出しますか？(qで終了)：")
    if key == "":
        continue
    elif key == "q":
        print("終了しました。")
        break
    try:
        value = fruit.pop(key)
        print(f"{key}は{value}個")
    except KeyError:
        print(f"{key}はありません。")
    except Exception as error:
        print(error)
        break
else: # whileループの終了後に実行
    print("もう空っぽです。")

fruit = {"apple":7, "orange":5, "peach":6}
while fruit: # fruitが空でなければ繰り返す
    ans = input("フルーツを取り出しますか？(y/n)：")
    if ans == "y":
        key, value = fruit.popitem()
        print(f"{key}は{value}個")
    elif ans == "n":
        print("終了しました。")
        break
else: # whileループの終了後に実行
    print("もう空っぽです。")