# データベース接続モジュールのインポート
import MySQLdb

# 基本設定
USER = "root" # ユーザー名
PASSWORD = "Pa$$w0rd"# パスワード
HOST = "localhost" # 接続
DB = "psysdb" # 接続先データベース名
CHARSET = "utf8" # 設定文字コード

## データベース接続処理
try:
    conn = MySQLdb.connect(
        user = USER,
        password = PASSWORD,
        host = HOST,
        db = DB,
        charset = CHARSET,
    )

    cursor = conn.cursor()

    print("データベース接続成功")

    ## SQLの作成
    sql = "select * from employee;"

    ## SQLの発行
    cursor.execute(sql,)

    ## 結果の取得
    rows = cursor.fetchall() # 全行分のデータをタプルで取得
    print(rows)

    if len(rows) != 0:
        for row in rows:
            print(row)
    else:
        print("データがありません。")

except:
    print("データベース接続失敗")