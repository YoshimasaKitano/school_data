import sqlite3

"""
このファイルは、もしデータベースがなければ、データベースを作成する関数が書かれたコードです。
もし、データベースがすでに存在する場合は作成されません。
テーブルはid,url,title,text,category,subcategory,updated_atでそれぞれ
プライマルキー、どこのページのものか、見出し、内容、カテゴリー、サブカテゴリー、最後に編集された時間が入ります。
"""

def create_database(database):
    conn = sqlite3.connect(database)

    # カーソル作成
    cur = conn.cursor()

    # テーブル作成例
    cur.execute("""
    CREATE TABLE IF NOT EXISTS articles (
        id INTEGER PRIMARY KEY,
        url TEXT,
        title TEXT,
        text TEXT,
        category TEXT,
        subcategory TEXT,
        updated_at DATETIME DEFAULT (datetime('now', 'localtime'))
    )
    """)

    # 保存して閉じる
    conn.commit()
    conn.close()