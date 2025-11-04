# データベース接続モジュールのインポート
import connect_db as db

## データベース接続処理
employee_no = input("従業員番号を入力→")
employee_name = input("名前を入力→")
password = input("パスワードを入力→")

res = db.insert_no(employee_no, employee_name, password)

if res == True:
    print("追加成功")
else:
    print("追加失敗")