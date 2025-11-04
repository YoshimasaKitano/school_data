# データベース接続モジュールのインポート
import connect_db as db

## データベース接続処理
rows = db.selectall()
print(rows)

if len(rows) != 0:
    for row in rows:
        print(row[0], row[1], row[2], row[3])
else:
    print("データがありません。")

"""

"""