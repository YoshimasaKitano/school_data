# データベース接続モジュールのインポート
import connect_db as db

## データベース接続処理
employee_no = input("従業員番号を入力→")
res = db.delete_no(employee_no)

if res == True:
    print("削除成功")
else:
    print("削除失敗")
