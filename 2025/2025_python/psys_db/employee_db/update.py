# データベース接続モジュールのインポート
import connect_db as db

## データベース接続処理
password = input("パスワードを入力→")
employee_no = input("従業員番号を入力→")

res = db.update_no(password, employee_no)

if res == True:
    print("更新成功")
else:
    print("更新失敗")