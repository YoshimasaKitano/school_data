# データベース接続モジュールのインポート
import connect_db as db

## データベース接続処理
stock = input("在庫を入力→")
item_code = input("商品番号を入力→")

res = db.update_no(stock, item_code)

if res == True:
    print("更新成功")
else:
    print("更新失敗")