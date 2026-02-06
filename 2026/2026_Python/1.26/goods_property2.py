### goods_property2.py

class Goods:

    # 初期化メソッド
    def __init__(self, name, price):
        self.__data = {"name":name, "price":price}

    ## nameのゲッターとセッター
    def get_name(self):
        return self.__data['name']

    def set_name(self, value):
        self.__data["name"] = value

    ## priceのゲッター
    def get_price(self):
        return self.__data["price"]

    name = property(get_name, set_name)
    price = property(get_price)


# インスタンスを生成
item = Goods("dream", 6800)
print(f"名前:{item.name}, 価格:{item.price}円") ### 名前:dream, 価格:6800円

## 名前を更新
item.name = "workman"
print(f"名前:{item.name}, 価格:{item.price}円") ### 名前:workman, 価格:6800円

