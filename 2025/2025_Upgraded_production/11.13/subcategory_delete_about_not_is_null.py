def delete_about_not_is_null():
    import sqlite3

    # === 設定 ===
    DB_PATH = "oca_test_data.db"  # ← .dbファイルのパスに書き換えてください

    # === DB接続 ===
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # 削除前の件数確認
    cursor.execute("SELECT COUNT(*) FROM articles WHERE subcategory IS  NOT NULL;")
    count_before = cursor.fetchone()[0]
    print(f"削除対象（subcategoryがNULLではない行）: {count_before}件")

    # === 削除実行 ===
    cursor.execute("DELETE FROM articles WHERE subcategory IS NOT NULL;")

    # === コミットして確定 ===
    conn.commit()

    # 削除後の確認
    cursor.execute("SELECT COUNT(*) FROM articles WHERE subcategory IS NULL;")
    count_after = cursor.fetchone()[0]

    print(f"削除完了。残りのsubcategory=NULL行: {count_after}件")

    # === 接続を閉じる ===
    conn.close()