# データベース接続モジュールのインポート
import connect_db as db

item_code = input("従業員番号を入力→")
## データベース接続処理
row = db.select_no(item_code)
print(row)

if row != None:
    print("商品番号:", row[0])
    print("商品名:", row[1])
    print("値段:", row[2])
    print("在庫:", row[3])
else:
    print("データがありません")