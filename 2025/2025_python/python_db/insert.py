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
    sql = "insert into employee values(%s, %s, %s);"

    ## SQLの発行
    employee_no = 'R40001'
    employee_name = '竹國聡子'
    password = 'zz0001'
    cursor.execute(sql,(employee_no, employee_name, password))

    ## SQLの実行
    conn.commit()

except:
    print("データベース接続失敗")