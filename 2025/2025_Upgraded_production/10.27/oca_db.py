import sqlite3

# データベースファイルの作成（なければ新規作成される）
conn = sqlite3.connect("oca_data.db")

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
