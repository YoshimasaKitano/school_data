### function_practice01.py
"""練習1
第1引数に底辺の長さ、第2引数に高さの数値を渡し
三角形の面積を表示する関数areaを作成する
"""
def area(bottom, high):
    area = (bottom * high) * 0.5
    print(area)
area(10, 20) 

"""練習2
第1引数にサイズ、第2引数に表示する文字を渡し
三角形の図形を表示する関数triangle()を作成する

[実行例]
triangle(3, "A")

A
AA
AAA
"""
def triangle(size, text):
    for i in range(1, size + 1):
        print(text * i)

triangle(3, "A")

# 模範解答
def triangle(size, char):
    for i in range(1, size+1):
        for j in range(i):
            print(char, end="")

        print()

# 関数の呼び出し
triangle(3, "A")
triangle(5, "B")


