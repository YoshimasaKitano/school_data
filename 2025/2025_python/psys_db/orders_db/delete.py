# データベース接続モジュールのインポート
import connect_db as db

## データベース接続処理
item_code = input("従業員番号を入力→")
res = db.delete_no(item_code)

if res == True:
    print("削除成功")
else:
    print("削除失敗")
