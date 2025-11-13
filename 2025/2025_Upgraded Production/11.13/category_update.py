def category_update():
    import sqlite3

    DB_PATH = "oca_test_data.db"  # ← あなたのDBファイルのパスに変更

    # === DB接続 ===
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # === 更新処理 ===
    cursor.execute("""
        UPDATE articles
        SET category = '学校概要'
        WHERE (subcategory IS NULL OR subcategory = '')
        AND category LIKE '%専攻情報%';
    """)

    # === コミットして確定 ===
    conn.commit()

    print("subcategory が空で、category に『専攻情報』を含む行の category を『学校概要』に変更しました。")

    # === 接続を閉じる ===
    conn.close()