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
    sql = "select * from employee where employee_no = %s;"

    ## SQLの発行
    id = 'R40001'
    cursor.execute(sql,(id,))

    ## 結果の取得
    row = cursor.fetchone() # 1行分のデータをタプルで取得
    print(row)
    
    if row != None:
        print(row[0])
        print(row[1])
        print(row[2])
    else:
        print("データがありません")

except:
    print("データベース接続失敗")