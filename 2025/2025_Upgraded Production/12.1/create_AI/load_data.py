import sqlite3
import json

def export_db_to_json(db_path: str, output_json: str):
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    # 全レコード取得
    cur.execute("SELECT * FROM articles")
    rows = cur.fetchall()

    # Row → dict に変換
    data = [dict(row) for row in rows]

    # JSON に保存（日本語もそのまま）
    with open(output_json, "w", encoding="utf-8") as fileobj:
        json.dump(data, fileobj, ensure_ascii=False, indent=2)

    conn.close()
    print(f"Exported {len(data)} records → {output_json}")


# 使い方例
export_db_to_json("test_oca.db", "articles.json")
