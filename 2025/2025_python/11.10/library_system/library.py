"""
図書館管理システム
"""
# モジュール
import os
import json

# ファイルの指定
BOOKS_FILE = "./books.json"
USERS_FILE = "./users.json"

## 各関数の定義
# ユーザーのデータを読み込む
def load_data(file):
    if os.path.exists(file):
        try:
            with open(file, "r", encoding  = "utf-8") as fileobj:
                data = json.load(fileobj) # JSON形式で読み込んで辞書型にする
                return data
        except:
            print("※ データファイルが破損、新しいファイルを作成します。")

    return {}

# ユーザーのデータをファイルに保存する関数
def save_data(file, data):
    try:
        with open(file, "w", encoding = "utf-8") as fileobj:
            # JSON形式でファイルに書き込む(保存)
            json.dump(data, fileobj, indent = 2, ensure_ascii = False)
    except:
        print("※ データの保存に失敗しました。")   

# 本の追加処理を行う関数
def add_book(books):
    title = input("タイトルを入力してください。")
    author = input("著者を入力してください。")
     
    books = load_data(BOOKS_FILE)
    if books:
        if title in books:
            print("すでに登録されています。")
        else:
            books[title] = {"author": author, "available": True}
            save_data(BOOKS_FILE, books)
            print("追加しました。")
    else:
        books[title] = {"author": author, "available": True}
        save_data(BOOKS_FILE, books)
        print("追加しました。")

# 本の検索処理を行う関数
def search_books(books):
    key = input("キーワードを入力してください。")

    books = load_data(BOOKS_FILE)
    for book in books:
        if key in book:
            title = book
            author = books[title]["author"]
            available = books[title]["available"]
            print(f"タイトル：{title}")
            print(f"著者名：{author}")
            print(f"貸し出し可否：{available}")
        else:
            print("キーワードに一致するタイトルが見つかりませんでした。")

# 本の削除処理を行う関数
def delete_book(books):
    title = input("タイトルを入力してください。")

    books = load_data(BOOKS_FILE)
    for book in books:
        if title == book:
            del books[title]
            save_data(BOOKS_FILE, books)
            print("削除しました。")
            break
        else:
            print("見つかりません。")
            break

# 本の更新処理を行う関数
def update_book(books):
    title = input("タイトルを入力してください。")
    new_author = input("新しい著者名を入力してください。")

    books = load_data(BOOKS_FILE)
    if title in books:
        books[title]["author"] = new_author
        save_data(BOOKS_FILE, books)
        print("更新しました。")
    else:
        print("見つかりません。")

# 本を借りる処理を行う関数
def borrow_book(books, users, username):
    title = input("タイトルを入力してください。")
    books = load_data(BOOKS_FILE)
    users = load_data(USERS_FILE)
    if users:
        if (books[title]["available"] == False) or (title not in books):
            print("貸出できません。")
        elif 0 < len(users[username]["borrowed"]) < 3:
            books[title]["available"] = False
            users[username]["borrowed"].append(title)
            save_data(BOOKS_FILE, books)
            save_data(USERS_FILE, users)
            print("貸出しました。")
        elif len(users[username]["borrowed"]) == 3:
            print("最大3冊までです。返却してください。")
    else:
        users[username] = {"borrowed": []}
        books[title]["available"] = False
        users[username]["borrowed"].append(title)
        save_data(BOOKS_FILE, books)
        save_data(USERS_FILE, users)
        print("貸出しました。")

# 本の返却処理を行う関数
def return_book(books, users, username):
    title = input("タイトルを入力してください。")
    books = load_data(BOOKS_FILE)
    users = load_data(USERS_FILE)
    for borrowed in users[username]["borrowed"]:
        if title in borrowed:
            books[title]["available"] = True
            users[username]["borrowed"].remove(title)
            save_data(BOOKS_FILE, books)
            save_data(USERS_FILE, users)
            print("返却しました。")
            break
        else:
            print("借りていません。")

# 管理者機能の制御処理をする関数
def admin_menu():
    while True:
        try:
            admin_mode = int(input("@管理者メニュー\n1. 本を追加\n2. 本を検索\n3. 本を削除\n4. 本を更新\n5. 戻る\n選択: [1-5]"))
        except:
            print("数字で入力して下さい。")
            continue
        if admin_mode == 1 or 2 or 3 or 4 or 5:
            if admin_mode == 1:
                add_book(BOOKS_FILE)
            elif admin_mode == 2:
                search_books(BOOKS_FILE)
            elif admin_mode == 3:
                delete_book(BOOKS_FILE)
            elif admin_mode == 4:
                update_book(BOOKS_FILE)
            else:
                break
        else:
            print("無効な選択です。")
            continue
    # if admin_mode == 5:
    #     main()

# ユーザー機能の制御処理をする関数
def user_menu(name):
    while True:
        try:
            user_mode = int(input(f"@ユーザー: [{name}]\n1. 本を借りる\n2. 本を返却する\n3. 貸出履歴を見る\n4. 戻る\n選択: [1-4]"))
        except:
            print("数字で入力して下さい。")
            continue
        if user_mode == 1 or 2 or 3 or 4:
            if user_mode == 1:
                borrow_book(BOOKS_FILE, USERS_FILE, name)
            elif user_mode == 2:
                return_book(BOOKS_FILE, USERS_FILE, name)
            elif user_mode == 3:
                users = load_data(USERS_FILE)
                if users[name]["borrowed"]:
                    print("現在借りている本は下記の通りです。")
                    for borrowed in users[name]["borrowed"]:
                        print(borrowed, end=",")
                    user_menu(name)
                else:
                    print("現在借りている本はありません。")
                    user_menu(name)
            else:
                break
        else:
            print("無効な選択です。")
            continue

# メイン処理の関数
def main():
    # 管理者モードかユーザーモードかの選択
    while True:
        try:
            mode = int(input("** 図書館システム **\n1. 管理者モード\n2. ユーザーモード\n3. 終了\n選択: [1-3]"))
        except:
            print("数字で入力して下さい。")
            continue
        if mode == 1 or 2 or 3:
            # 管理者モードの場合、管理者メニューを表示する
            if mode == 1:
                admin_menu()
            # ユーザーモードの場合、ユーザーメニューを表示する
            elif mode == 2:
                users = load_data(USERS_FILE)
                name = input("あなたの名前を入力してください→")
                if name in users:
                    user_menu(name)
                else:
                    print("新規ユーザー登録しました。")
                    user_menu(name)
            else:
                break
        else:
            print("無効な選択です。")
            continue

# このファイルがスクリプトとして実行された場合のみmain()を呼び出す
if __name__ == "__main__":
    main()