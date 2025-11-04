# データベース接続モジュールのインポート
import connect_db as db

## データベース接続処理
item_code = input("商品番号を入力→")
item_name = input("商品名を入力→")
price = input("値段を入力→")
stock = input("在庫を入力→")

res = db.insert_no(item_code, item_name, price, stock)

if res == True:
    print("追加成功")
else:
    print("追加失敗")