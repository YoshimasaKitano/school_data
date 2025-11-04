## function_sample02.py
# 関数で使う変数の有効範囲:スコープ
v = 10 # グローバル変数
def calc():
    v = 2 # ローカル変数
    ans = 3 * v
    print(ans)

calc() ### 6
print(v) ### 10

# 関数でグローバル変数を使う
def calc2():
    global v # グローバル変数のvを呼び出す
    ans = 3* v
    print(ans)

calc2() ### 30

## 引数について
# 位置引数
def price(adult, child):
    return (adult * 1200) + (child * 500)

print(price(1, 2)) ### 2200 大人が1人、子供が2人

print(price(2, 1)) ### 2900 大人が2人、子供が1人

# キーワード引数
def price2(adult, child):
    return (adult * 1200) + (child * 500)

print(price2(adult=1, child=2)) ### 2200
print(price2(adult=2, child=1)) ### 2200

# 初期値のある引数
def price3(adult=1, child=1): # 関数を定義する際に初期値を設定する
    return (adult * 1200) + (child * 500)

print(price3()) ### 1700 初期値の値で実行される
print(price3(1, 2)) ### 2200 引数の値で実行される
print(price3(adult=1, child=2)) ### 2200

# キーワード引数を利用して特定の引数だけ指定する
def calc(size = "M", num = 6): # 初期値が設定されている
    unit_price = {"s":120, "M":150, "L":180}
    price = unit_price[size] * num
    return (size, num, price) # 戻り値がタプル型

# 関数の呼び出し1
a = calc()
print(f"size:{a[0]}, num{a[1]}, price:{a[2]}") ### size:M, num6, price:900

# 関数の呼び出し2
b = calc("L")
print(f"size:{b[0]}, num{b[1]}, price:{a[2]}") ### size:L, num6, price:900

# 関数の呼び出し3
c = calc(num = 1)
print(f"size{c[0]}, num{c[1]}, price:{c[2]}") ### sizeM, num1, price:150

## 引数の個数を固定しない関数:可変長引数
def fruits(*args): # *args 可変長引数
    print(args) # タプル型で表示される

# 関数の呼び出し
fruits() ### ()
fruits("りんご","みかん") ### ('りんご', 'みかん')
fruits("りんご", "みかん","いちご", "ばなな" ) ### ('りんご', 'みかん', 'いちご', 'ばなな')

## 可変長引数を辞書型で渡す
def fruits2(**kwargs): # *args 可変長引数
    print(kwargs) # 辞書型で表示される

# 関数の呼び出し
fruits2() ### {} 

# 引数にキーワード引数を使う
fruits2(apple = 2, orange = 3, banana = 1) ### {'apple': 2, 'orange': 3, 'banana': 1}

# 必須の引数と可変長引数を組み合わせる
def entry(name, gender, **kwargs):
    data = {"name":name, "gender":gender}
    data.update(kwargs)
    return data

# 関数の呼び出し
dict_data = entry(name="小野田坂道", gender="男性", age=18, hobby="自転車")
print(dict_data) ### {'name': '小野田坂道', 'gender': '男性', 'age': 18, 'hobby': '自転車'}

