def in_database():
    # 使うものをすべてimportする。
    # requests,bs4,transformers,torch
    import requests
    from bs4 import BeautifulSoup
    from urllib.parse import urljoin, urlparse
    import json
    import os
    from transformers import pipeline
    import re
    from get_url_def import get_url
    from get_html_def import scrape_from_heading
    from classifer_def import classify
    from subclassifer_def import subclassify
    import sqlite3
    from create_db_def import create_database

    # 定数の指定
    DATA_FILE = "./data/scraped.json"

    while True:
        try:      
            url = input("URLを入力してください: ")
            db = (input("データベースの名前を入力してください(.dbは自動で入力されます): ")) + ".db"
            break
        except:
            print("URLが正しく読み込まれないか、データベースの名前の指定が間違っています。正しく入力してください")
            continue
    
    # データベースの作成
    create_database(db)

    # URL取得
    print("URLを取得中・・・")
    urls = get_url(url)
        
    # URLごとにスクレイピング
    print("スクレイピングデータを保存中")
    for i in range(len(urls)):
        scrape_url = urls[i]
        scrape_from_heading(scrape_url, output_filename="scraped.json")

        # カテゴリー分け
        classify_category = classify(use_model=False)

        ## カテゴリー分けのエラーチェック
        if classify_category["error"]:
            print(f"{urls[i]}でカテゴリー分けでエラーがあります!")
            break

        # サブカテゴリー分け
        classify_subcategory = subclassify()

        ## サブカテゴリー分けのエラーチェック
        if classify_subcategory["error"]:
            print(f"{urls[i]}でサブカテゴリー分けでエラーがあります!")
            break
            
        # DBの格納
        try:
            ## jsonファイルの読み込み
            with open(DATA_FILE, "r", encoding="utf-8") as fileobj:
                data = json.load(fileobj)

            conn = sqlite3.connect("./" + db)
            cursor = conn.cursor()

            ## データベースに値を入力する
            for item in data:
                url = urls[i]
                title = classify_category["used_text"]
                text = item.get("text")
                category = classify_category["category"]
                subcategory = classify_subcategory["subcategory"]
                cursor.execute("""
                    INSERT INTO articles (url, title, text, category, subcategory)
                    VALUES (?,?,?,?,?)
                """,(
                    url,
                    title,
                    text,
                    category,
                    subcategory
                ))
            conn.commit()
            conn.close()
        except:
            print(f"{urls[i]}にてデータベースの書き込みまたはjsonファイルの読み込みに失敗しました。")

# 実行テスト
in_database()
