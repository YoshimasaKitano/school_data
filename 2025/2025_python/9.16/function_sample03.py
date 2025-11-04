### function_sample03.py
## 関数オブジェクト
def hello():
    print("ハロー")

# 関数の呼び出し
hello() ### ハロー

# 変数msgに関数helloを代入する
msg = hello

msg() ### ハロー

def thanks():
    print("ありがとう")

def hi():
    print("やあ!")

# 関数オブジェクトを引数にその関数を呼び出す関数
def do(func):
    func()

# 関数の呼び出し
do(thanks) ### ありがとう
do(hi) ### やあ!
do(hello) ### ハロー
do(msg) ### ハロー

## 引数と戻り値がある場合
def child(arg):
    return 400 * arg

def adult(arg):
    return 1200 * arg

# 関数オブジェクトを引数にその関数を呼び出す関数
def calc(func, arg):
    price = func(arg)
    return price

# 関数を呼び出す
price = calc(child, 3)
print(price) ### 1200

print(calc(adult, 2)) ### 2400

## クロージャー(関数閉包)
def charge(price):

    def calc(num):
        return price * num
    
    return calc

child = charge(400)
price_child = child(3)
print(price_child) ### 1200

adult = charge(1200)
print (adult(2)) ### 2400

## ラムダ式(無名関数)
# 普通の関数
def area(w, h):
    return w * h

num = area(3, 4)
print (num) ### 12

# ラムダ式1
func = lambda w, h : w * h
num = func(3, 4)
print(num) ### 12

# ラムダ式2
num = (lambda w, h : w * h)(3, 4)
print(num) ### 12

## ラムダ式の引数に初期値を設定する
print((lambda w = 3, h = 4 : w * h)()) ### 12
print((lambda w = 3, h = 4 : w * h)(2, 5)) ### 10

"""練習1
2つの引数を合計して返す関数add()を定義
関数オブジェクトとして変数operationに代入
operationに引数10と20を渡して結果を表示する
"""

def add(num1, num2):
    return num1 + num2

operation = add

print(operation(10, 20)) ### 30

"""練習2
引数に数値xを持つ関数make()を定義
この関数の中に関数multi(y)を定義、この関数はxとyを掛けた結果を返す
make()に引数10を渡し、multi()に引数5を渡し結果を表示する
"""

def make(x):
    def multi(y):
        return x * y
    return multi
print((make(10))(5)) ### 50

"""練習3
引数が偶数の場合Trueを返す関数is_even()を定義する
"""
def is_even(num):
    if num % 2 == 0:
        return True
print (is_even(2)) ### True

# 模範解答
def is_even(num):
    return num % 2 == 0
print(is_even(2)) ### True

"""練習4
練習3の関数をラムダ式に書き換える
"""
print((lambda num : True if num % 2 == 0 else False)(2)) ### True

# 模範解答
is_even = lambda num : num % 2 == 0
print(is_even(2)) ### True

## ソート関数を作る
def size(item):
    sizelist = ["XS", "S", "M", "L"]
    return sizelist.index(item)

# 並び変えるリスト
data = ["S", "M", "XS", "L", "M", "M", "XS", "S", "M", "L", "M"]

# 普通にソートするとアルファベット順になる
data.sort()
print(data) ### ['L', 'L', 'M', 'M', 'M', 'M', 'M', 'S', 'S', 'XS', 'XS']

# 基準となる関数オブジェクトを引数に渡す
data.sort(key=size)
print(data) ### ['XS', 'XS', 'S', 'S', 'M', 'M', 'M', 'M', 'M', 'L', 'L']

# ラムダ式
sizelist = ["XS", "S", "M", "L"] # 並び替えの基準となるリスト
data = ["S", "M", "XS", "L", "M", "M", "XS", "S", "M", "L", "M"] # 並び替えるリスト

data.sort(key= lambda item : sizelist.index(item))
print(data) ### ['XS', 'XS', 'S', 'S', 'M', 'M', 'M', 'M', 'M', 'L', 'L']

## map(関数,イテラブル)
# リストの要素を2倍にする
# 関数
def double(x):
    return x * 2

# イテラブル
nums = [4, 3, 7, 6, 2, 1]

map_data = map(double, nums)
print(map_data) ### <map object at 0x0000024F4AA31E40>
print(list(map_data)) ### [8, 6, 14, 12, 4, 2]

# ラムダ式
print(list(map(lambda x:x * 2, nums))) ### [8, 6, 14, 12, 4, 2]

# リスト内包表記
nums2 = [num * 2 for num in nums]
print(nums2) ### [8, 6, 14, 12, 4, 2]

## filter(関数, イテラブル)
# numsから正の値だけを抜き出してリストを作る
nums = [4, -3, 9, -2, -4, 5]
nums2 = list(filter(lambda x : x > 0, nums))
print(nums2) ### [4, 9, 5]

# リスト内包表記
nums = [4, -3, 9, -2, -4, 5]
nums2 = [num for num in nums if num > 0]
print(nums2) ### [4, 9, 5]
