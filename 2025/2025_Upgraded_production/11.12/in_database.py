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
            url = input("URLを入力してください")
            db = (input("データベースの名前を入力してください(.dbは自動で入力されます)")) + ".db"
            break
        except:
            print("URLが正しく読み込まれないか、データベースの名前の指定が間違っています。正しく入力してください")
            continue


    # URL取得
    try:
        urls = get_url(url)

        # URLごとにスクレイピング
        for i in range(len(urls)):
            try:
                scrape_url = urls[i]
                scrape_from_heading(scrape_url, output_filename="scraped.json")
                print(f"{urls[i]}を処理中")
                # カテゴリー分け
                try:
                    classify_category = classify(use_model=False)
                    # エラーチェック
                    if classify_category["error"]:
                        print("カテゴリー分けでエラーがあります!")
                        break
                    # サブカテゴリー分け
                    try:
                        classify_subcategory = subclassify()
                        if classify_subcategory["error"]:
                            print("サブカテゴリー分けでエラーがあります!")
                            break
                        
                        try:
                            # DBの作成
                            create_database(db)

                            try:
                                # DBの格納
                                with open(DATA_FILE, "r", encoding="utf-8") as fileobj:
                                    data = json.load(fileobj)

                                conn = sqlite3.connect("./" + db)
                                cursor = conn.cursor()

                                for item in data:
                                    url = urls[i]
                                    title = classify_category["used_text"] ###エラー文を検知する仕組みを作らないと
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
                                print("データベースに書き込めませんでした")

                        except:
                            print("データベースが作成できませんでした")
                    except:
                        print("サブカテゴリー分けができません")
                except:
                    print("カテゴリー分けができません")
            except:
                print("スクレイピングができません")
    except:
        print("URLが取得できません")
    

in_database()
