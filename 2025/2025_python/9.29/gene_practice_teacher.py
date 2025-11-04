### gene_practice.py
""" 練習問題1
・引数で指定された範囲内の偶数を順に返すジェネレータ関数 even_gene(start,end) を作成せよ。
・ジェネレータ関数 even_gene を使ってジェネレータを生成し、そのすべての値を順に表示せよ。
"""
# 関数の定義
def even_gene(start,end):
    for i in range(start,end + 1): # startからendまでの値を取得
        if i%2==0: # 偶数の判定
            yield i # 偶数だけを返す

# 関数を呼出して表示
gene = even_gene(3,15)
print(type(gene)) ### <class 'generator'>

print(next(gene)) ### 4
print(next(gene)) ### 6
for i in gene:
    print(i)
"""
8
10
12
14
"""

""" 練習問題2
・与えられた文字列を逆順に1文字ずつ返すジェネレータ関数 reverse_string(text) を作成せよ。
・ジェネレータ関数 reverse_string を使ってジェネレータを生成し、そのすべての文字を順に表示せよ。
例）python → nohtyp
"""
# 関数の定義
def reverse_string(text):
    for ch in text[::-1]: # 文字列を逆並びにスライスする
        yield ch # 1文字づつ返す

# 関数を呼出して表示
gene = reverse_string("Python")
print(type(gene)) ### <class 'generator'>

print(next(gene)) ### n
print(next(gene)) ### o
for ch in gene:
    print(ch, end="") ### htyP

print() ### 改行

""" 練習問題3
・与えられた文字列から、母音（a, e, i, o, u）だけを大文字に変換し、
  それ以外の文字はそのまま返すジェネレータ関数 convert_gen(text) を作成せよ。
・ジェネレータ関数 convert_gen を使ってジェネレータを生成し、すべての文字を順に表示せよ。
例）"python is fun" → "pythOn Is fUn"
"""
# 関数の定義
def convert_gen(text):
    text = text.lower() # 小文字に変換
    for ch in text: # textから1文字づつ取得
        if ch in "aeiou":
            yield ch.upper() # 大文字して返す
        else:
            yield ch # そのまま返す

# 関数を呼出して表示
gene = convert_gen("python is fun")
print(type(gene)) ### <class 'generator'>

for ch in gene:
    print(ch, end="") ### pythOn Is fUn 

print() # 改行

""" 練習問題4
・練習問題3のジェネレータ関数をジェネレータ式で記述
"""
# 関数の定義
text = "python is fun"
gene = (ch.upper() if ch.lower() in "aeiou" else ch for ch in text)

# 関数を呼出して表示
print(type(gene)) ### <class 'generator'> 
for ch in gene:
    print(ch, end="") ### pythOn Is fUn

print()
