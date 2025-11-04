# iter_practice.py
""" 練習問題1
・引数で指定された範囲内の偶数を順に返すイテレータを生成する関数 even_iter(start,end) を作成せよ。
・関数 even_iter から生成したイテレータを使い、すべての値を順に表示せよ。
"""
# 関数の定義
def even_iter(start,end):
    # 偶数のリストを作る
    numbers = []
    for i in range(start,end + 1):
        if i%2==0:
            numbers.append(i)

    return iter(numbers) # イテレータを返す

# 関数を呼出して表示
iter_data = even_iter(3,15)
print(type(iter_data)) ### <class 'list_iterator'>

while True:
    try:
        print(next(iter_data))
    except StopIteration:
        break

"""
4
6
8
10
12
14
"""


""" 練習問題2
・与えられた文字列を逆順に1文字ずつ返すイテレータを生成する関数 reverse_iter(text) を作成せよ。
・関数 reverse_iter から生成したイテレータを使い、すべての文字を順に表示せよ。
例）python → nohtyp
"""
# 関数の定義
def reverse_iter(text):
    # list_data = list(text[::-1])
    # return iter(list_data)
    return iter(text[::-1])

# 関数を呼出して表示
# for char in reverse_iter("Python"):
#     print(char,end="")

iter_data = reverse_iter("Python")
for char in iter_data:
    print(char,end="")

print() # 横並びを切るための改行
"""
nohtyP
"""

""" 練習問題3
・与えられた文字列から、母音（a, e, i, o, u）だけを大文字に変換し、
  それ以外の文字はそのまま返すイテレータを生成する関数 convert_iter(text) を作成せよ。
・関数 convert_iter から生成したイテレータを使い、すべての文字を順に表示せよ。
例）"python is fun" → "pythOn Is fUn"
"""
# 関数の定義
def convert_iter(text):
    text = text.lower() # 小文字に変換
    converted = []
    for ch in text: # textから1文字づつ取得
        if ch in "aeiou":
            converted.append(ch.upper()) # リストに大文字にして追加
        else:
            converted.append(ch) # そのままリストに追加

    return iter(converted) # イテレータに変換して返す

# 関数を呼出して表示
for ch in convert_iter("python is fun"):
    print(ch, end="")

print() # 横並びを切るための改行

### pythOn Is fUn

