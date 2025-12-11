def update_and_delete_about_major():
    import sqlite3
    import re

    DB_PATH = "oca_notnull.db"  # ← DBファイルのパスに変更

    # === DB接続 ===
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # subcategoryがNULLでない行を取得
    cursor.execute("SELECT id, subcategory FROM articles WHERE subcategory IS NOT NULL;")
    rows = cursor.fetchall()

    updated_count = 0
    deleted_count = 0

    for article_id, subcategory in rows:
        # 「&」を含むパターンにも対応した正規表現
        # e.g. "e-sports & プログラミング専攻" → "e-sports & プログラミング専攻"
        # 通常の "〇〇専攻" も拾える
        match = re.search(
            r"([A-Za-z0-9一-龥ぁ-んァ-ンー・\s\-&＆]+?専攻)", 
            subcategory
        )   

    if match:
        new_subcategory = match.group(1).strip()

        # 不要な連続スペースや「　」（全角空白）を整理
        new_subcategory = re.sub(r"\s+", " ", new_subcategory)

        # 変化がある場合のみ更新
        if new_subcategory != subcategory:
            cursor.execute(
                "UPDATE articles SET subcategory = ? WHERE id = ?;",
                (new_subcategory, article_id)
            )
            updated_count += 1
    else:
        # 「専攻」を含まない行を削除
        cursor.execute("DELETE FROM articles WHERE id = ?;", (article_id,))
        deleted_count += 1

    # コミット
    conn.commit()

    print(f"✅ subcategoryを更新しました（{updated_count}件変更）")
    print(f"🗑️  '専攻' が含まれない行を削除しました（{deleted_count}件削除）")

    conn.close()
