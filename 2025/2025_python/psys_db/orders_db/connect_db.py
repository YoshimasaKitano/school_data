# データベース接続モジュールのインポート
import MySQLdb

# 基本設定
USER = "root" # ユーザー名
PASSWORD = "Pa$$w0rd"# パスワード
HOST = "localhost" # 接続
DB = "psysdb" # 接続先データベース名
CHARSET = "utf8" # 設定文字コード

## データベース接続処理
# itemテーブルのデータ一覧
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
        sql = "select * from orders;"

        ## SQLの発行
        cursor.execute(sql,)

        ## 結果の取得
        rows = cursor.fetchall() # 全行分のデータをタプルで取得


    except Exception as e:
        print("データベース接続失敗")
        print(e)

    return rows

# itemテーブルの特定の商品番号のデータ一覧
def select_no(item_code):
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
        sql = "select * from item where item_code = %s;"

        ## SQLの発行
        cursor.execute(sql,(item_code,))

        ## 結果の取得
        row = cursor.fetchone() # 1行分のデータをタプルで取得

    except Exception as e:
        print("データベース接続失敗")
        print(e)

    return row

# itemテーブルの特定の商品番号のデータ削除
def delete_no(item_code):
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
        sql = "delete from item where item_code = %s;"

        ## SQLの発行
        cursor.execute(sql,(item_code,))


        ## SQLの実行
        conn.commit()
        res = True
    
    except Exception as e:
        print("データベース接続失敗")
        print(e)

    return res

# itemテーブルの特定の商品番号の在庫更新
def update_no(stock, item_code):
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
        sql = "update item set stock = %s where item_code = %s;"

        ## SQLの発行
        cursor.execute(sql,(stock, item_code))

        ## SQLの実行
        conn.commit()
        res = True
    
    except Exception as e:
        print("データベース接続失敗")
        print(e)

    return res

# itemテーブルのデータ追加
def insert_no(item_code, item_name, price, stock):
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
        sql = "insert into item values(%s, %s, %s, %s);"

        ## SQLの発行
        cursor.execute(sql,(item_code, item_name, price, stock))

        ## SQLの実行
        conn.commit()
        res = True

    except Exception as e:
        print("データベース接続失敗")
        print(e)

    return res