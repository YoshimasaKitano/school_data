### gene_practice.py
""" 練習問題1
・引数で指定された範囲内の偶数を順に返すジェネレータ関数 even_gene を作成せよ。
・ジェネレータ関数 even_gene を使ってジェネレータを生成し、そのすべての値を順に表示せよ。
"""
# 関数の定義
def even_gene(num1, num2):
    for i in range(num1, num2 + 1):
        if i % 2 == 0:
            yield i
        else:
            continue

# 関数を呼出して表示
num = even_gene(0, 10)
for i in num:
    print(i)



""" 練習問題2
・与えられた文字列を逆順に1文字ずつ返すジェネレータ関数 reverse_string を作成せよ。
・ジェネレータ関数 reverse_string を使ってジェネレータを生成し、そのすべての文字を順に表示せよ。
例）python → nohtyp
"""
# 関数の定義
def reverse_string(str):
    


# 関数を呼出して表示


""" 練習問題3
・与えられた文字列から、母音（a, e, i, o, u）だけを大文字に変換し、
  それ以外の文字はそのまま返すジェネレータ関数 convert_gen を作成せよ。
・ジェネレータ関数 convert_gen を使ってジェネレータを生成し、すべての文字を順に表示せよ。
例）"python is fun" → "pythOn Is fUn"
"""
# 関数の定義



# 関数を呼出して表示


""" 練習問題4
・練習問題3のジェネレータ関数をジェネレータ式で記述
"""
# 関数の定義



# 関数を呼出して表示

