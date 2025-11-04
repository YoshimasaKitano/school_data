# データベース接続モジュールのインポート
import connect_db as db

## データベース接続処理
rows = db.selectall()
print(rows)

if len(rows) != 0:
    for row in rows:
        print(row[0], row[1], row[2])
else:
    print("データがありません。")

"""
R20001 鈴木一郎 ry0001
R20002 山田太郎 rx0002
R20003 坂本竜馬 rw0003
R20004 田中花 rv0004
"""