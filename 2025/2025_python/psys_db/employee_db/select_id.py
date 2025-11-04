# データベース接続モジュールのインポート
import connect_db as db

emp_no = input("従業員番号を入力→")
## データベース接続処理
row = db.select_no(emp_no)
print(row)

if row != None:
    print("従業員番号:", row[0])
    print("従業員名:", row[1])
    print("パスワード:", row[2])
else:
    print("データがありません")