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

    # データの読み込み
    books = load_data(BOOKS_FILE)

    # booksの中に値があるかどうかの確認
    if books:

        # 同じタイトルの本の名前がbooksの中にある場合
        if title in books:
            print("すでに登録されています。")

        # 同じタイトルの本の名前が無ければ追加
        else:
            books[title] = {"author": author, "available": True}

            # データをファイルに保存
            save_data(BOOKS_FILE, books)
            print("追加しました。")

    # 値が無ければそのまま追加する
    else:
        books[title] = {"author": author, "available": True}

        # データをファイルに保存
        save_data(BOOKS_FILE, books)
        print("追加しました。")

# 本の検索処理を行う関数
def search_books(books):
    key = input("キーワードを入力してください。")

    # データの読み込み
    books = load_data(BOOKS_FILE)
 
    # カウンターの初期化
    count = 0

    # 読み込んだbooksファイルの中身をループで総当たり(keyに引っかかるものは全て表示するため)
    for book in books:

        # bookにkeyが含まれているか
        if key in book:
            title = book
            author = books[title]["author"]
            available = books[title]["available"]
            print(f"タイトル：{title}")
            print(f"著者名：{author}")
            print(f"貸し出し可否：{available}")
            print()

            # カウンターを使って1つでも含まれているものが見つかったか確認
            count += 1

    # カウンターが一つも増えていなかった＝一つも見つからなかった場合
    if count == 0:
        print("見つかりませんでした。")

# 本の削除処理を行う関数
def delete_book(books):
    title = input("タイトルを入力してください。")

    # データの読み込み
    books = load_data(BOOKS_FILE)

    # 削除処理を行いたい本を総当たりで見つける
    for book in books:

        # 削除したい本が貸出中の場合
        if book["available"] == False:
            print("現在その本は貸出中です。削除はできません。")
            break

        else:
            # 削除したい本が見つかった場合
            if title == book:
                del books[title]

                # データをファイルに保存
                save_data(BOOKS_FILE, books)
                print("削除しました。")
                break

            # 削除したい本が見つからなかった場合
            else:
                print("見つかりません。")
                break

# 本の更新処理を行う関数
def update_book(books):
    title = input("タイトルを入力してください。")
    new_author = input("新しい著者名を入力してください。")

    # データの読み込み
    books = load_data(BOOKS_FILE)

    # 更新したい本のタイトルが見つかった場合
    if title in books:
        books[title]["author"] = new_author

        # データをファイルに保存
        save_data(BOOKS_FILE, books)
        print("更新しました。")
    
    # 更新したい本のタイトルが見つかった場合
    else:
        print("見つかりません。")

# 本を借りる処理を行う関数
def borrow_book(books, users, username):
    title = input("タイトルを入力してください。")

    # データの読み込み
    books = load_data(BOOKS_FILE)
    users = load_data(USERS_FILE)

    # 本が貸出中または本が存在しない場合
    if (title not in books) or (books[title]["available"] == False):
        print("貸出できません。")
        
    # ユーザーの本を借りている冊数が0以上3未満の場合
    elif 0 <= len(users[username]["borrowed"]) < 3:
        books[title]["available"] = False
        users[username]["borrowed"].append(title)

        # データをファイルに保存
        save_data(BOOKS_FILE, books)
        save_data(USERS_FILE, users)
        print("貸出しました。")

    # ユーザーの本を借りている冊数が3冊の場合
    elif len(users[username]["borrowed"]) == 3:
        print("最大3冊までです。返却してください。")

# 本の返却処理を行う関数
def return_book(books, users, username):
    title = input("タイトルを入力してください。")

    # データの読み込み
    books = load_data(BOOKS_FILE)
    users = load_data(USERS_FILE)

    # ユーザーの借りている本の配列の要素数が1以上の時
    if len(users[username]["borrowed"]) >= 1:

        # ユーザーの借りている本を総当たりで確認
        for borrowed in users[username]["borrowed"]:

            # 指定したタイトルが借りている本のタイトルの配列にあった場合
            if title in borrowed:
                books[title]["available"] = True
                users[username]["borrowed"].remove(title)
            
                # データをファイルに保存
                save_data(BOOKS_FILE, books)
                save_data(USERS_FILE, users)
                print("返却しました。")
                break

            # 指定したタイトルが借りている本のタイトルの配列になかった場合
            else:
                print("その本は借りていません。")

    # ユーザーの借りている本の配列の要素数が1未満の時
    else:
        print("借りている本がありません。借りてください。")


# 管理者機能の制御処理をする関数
def admin_menu():
    while True:
        try:
            # 管理者機能の選択
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

# ユーザー機能の制御処理をする関数
def user_menu(name):
    while True:
        try:
            # ユーザー機能の選択
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

                # 借りている本がある場合
                if users[name]["borrowed"]:
                    print("現在借りている本は下記の通りです。")
                    for borrowed in users[name]["borrowed"]:
                        print(borrowed, end=",")

                # 借りている本が無い場合
                else:
                    print("現在借りている本はありません。")

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

                # データの読み込み
                users = load_data(USERS_FILE)
                name = input("あなたの名前を入力してください→")

                # 入力された名前がデータに存在する場合
                if name in users:
                    user_menu(name)

                # 入力された名前がデータに存在しない場合
                else:
                    # 新しいユーザーデータの作成
                    users[name] = {"borrowed": []}
                    save_data(USERS_FILE, users)
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