## function_sample01.py
# 引数なし　戻り値なしの関数の定義
def show_msg():
    print("引数なし、戻り値なしの関数") ### 引数なし、戻り値なしの関数

# 関数の呼び出し
show_msg()

# 引数あり、戻り値なしの関数の定義
def show_msg2(item, item2):
    print(item + "あり、" + item2 + "なしの関数")

# 関数の呼び出し
show_msg2("引数", "戻り値") ### 引数あり、戻り値なしの関数

# 引数なし、戻り値ありの関数の定義
def show_msg3():
    return "引数なし、戻り値ありの関数"

# 関数の呼び出し
print(show_msg3()) ### 引数なし、戻り値ありの関数
res = show_msg3()
print(res) ### 引数なし、戻り値ありの関数

# 引数あり、戻り値ありの関数の定義
def show_msg4(item1, item2):
    return item1 + "あり、" + item2 + "ありの関数"

# 関数の呼び出し
res = show_msg4("引数", "戻り値")
print(res) ### 引数あり、戻り値ありの関数

## 練習：数値を2つ引数の渡し、合計値を返す関数を定義
## 練習で定義した関数を呼び出して結果を表示する
def sum_item(item1, item2):
    return item1 + item2
sum = sum_item(10, 20)
print(sum) ### 30

# 模範解答
def renshu1(num1, num2):
    return num1 + num2

ans = renshu1(3, 5)
print("合計:" + str(ans)) ### 合計:8

ans = renshu1(2, 7)
print("合計:" + str(ans)) ### 合計:9

## 1辺の長さを引数に正方形の面積を表示する関数
## 練習2の関数を呼び出す
def square_area(num1):
    return num1 ** 2
area = square_area(5)
print("正方形の面積は" + str(area)) ### 正方形の面積は25

# 模範解答
def square(num):
    print("正方形の面積:", num * num)

square(5) ### 正方形の面積: 25
square(6) ### 正方形の面積: 36

## 中身のない関数
def empty():
    pass

empty()

# 引数が数値ではない場合Noneを返す関数
def calc(num):
    unit_price = 180
    if not num.isdigit(): # 数字で構成されている
        return None

    # 数値の場合は計算結果を返す
    price = int(num) * unit_price
    return price

while True:
    num = input("個数を入力(qで終了)→")

    if num == '': # 未入力チェック
        continue
    elif num == "q": # qの場合は処理を終了
        break

    result = calc(num) # キーボードで入力で所得した値で計算する
    print(result)

print("プログラム終了")


# 引数が数値ではない場合Noneを返す関数(浮動少数がたに変換)
def calc(num):
    unit_price = 180
    try:
        num = float(num) # 浮動小数型に変換
        return num * unit_price
    except:
        return None

while True:
    num = input("個数を入力(qで終了)→")

    if num == '': # 未入力チェック
        continue
    elif num == "q": # qの場合は処理を終了
        break

    result = calc(num) # キーボードで入力で所得した値で計算する
    print(result)

print("プログラム終了")