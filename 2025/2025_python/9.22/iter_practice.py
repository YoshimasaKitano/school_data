# iter_practice.py
""" 練習問題1
・引数で指定された範囲内の偶数を順に返すイテレータを生成する関数 even_iter を作成せよ。
・関数 even_iter から生成したイテレータを使い、すべての値を順に表示せよ。
"""
# 関数の定義
def even_gene(start, end):
    nums = []
    for i in range(start, end + 1):
        if i % 2 == 0:
            nums.append(i)
    return iter(nums)

# 関数を呼出して表示
for num in even_gene(0, 10):
    print(num)




""" 練習問題2
・与えられた文字列を逆順に1文字ずつ返すイテレータを生成する関数 reverse_iter を作成せよ。
・関数 reverse_iter から生成したイテレータを使い、すべての文字を順に表示せよ。
例）python → nohtyp
"""
# 関数の定義
def reverse_iter(str):
    list_str = list(str[::-1])
    return iter(list_str)
        


# 関数を呼出して表示
for i in reverse_iter("Python"):
    print(i, end="")


""" 練習問題3
・与えられた文字列から、母音（a, e, i, o, u）だけを大文字に変換し、
  それ以外の文字はそのまま返すイテレータを生成する関数 convert_iter を作成せよ。
・関数 convert_iter から生成したイテレータを使い、すべての文字を順に表示せよ。
例）"python is fun" → "pythOn Is fUn"
"""
# 関数の定義
def convert_iter(text):
    list_str = list(text)
    list_str_new = []
    for i in range(len(list_str)):
        if list_str[i] == "a" or "e" or "i" or "o" or "u":
            list_str_new.append(str((list_str.pop[i])).upper())



# 関数を呼出して表示
