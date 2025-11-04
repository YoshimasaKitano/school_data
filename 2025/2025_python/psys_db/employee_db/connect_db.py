# データベース接続モジュールのインポート
import MySQLdb

# 基本設定
USER = "root" # ユーザー名
PASSWORD = "Pa$$w0rd"# パスワード
HOST = "localhost" # 接続
DB = "psysdb" # 接続先データベース名
CHARSET = "utf8" # 設定文字コード

## データベース接続処理
# employeeテーブルのデータ一覧
def selectall():
    rows = None
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


    except Exception as e:
        print("データベース接続失敗")
        print(e)

    return rows

# employeeテーブルの特定の従業員のデータ一覧
def select_no(employee_no):
    row = None
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
        cursor.execute(sql,(employee_no,))

        ## 結果の取得
        row = cursor.fetchone() # 1行分のデータをタプルで取得

    except Exception as e:
        print("データベース接続失敗")
        print(e)

    return row

# employeeテーブルの特定の従業員のデータ削除
def delete_no(employee_no):
    res = False
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
        sql = "delete from employee where employee_no = %s;"

        ## SQLの発行
        cursor.execute(sql,(employee_no,))


        ## SQLの実行
        conn.commit()
        res = True
    
    except Exception as e:
        print("データベース接続失敗")
        print(e)

    return res

# employeeテーブルの特定の従業員のパスワード更新
def update_no(password, employee_no):
    res = False
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
        sql = "update employee set password = %s where employee_no = %s;"

        ## SQLの発行
        cursor.execute(sql,(password, employee_no))

        ## SQLの実行
        conn.commit()
        res = True
    
    except Exception as e:
        print("データベース接続失敗")
        print(e)

    return res

# employeeテーブルのデータ追加
def insert_no(employee_no, employee_name, password):
    res = False
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
        cursor.execute(sql,(employee_no, employee_name, password))

        ## SQLの実行
        conn.commit()
        res = True

    except Exception as e:
        print("データベース接続失敗")
        print(e)

    return res