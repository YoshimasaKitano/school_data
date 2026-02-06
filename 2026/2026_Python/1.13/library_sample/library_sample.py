# モジュール
import json
import os

# --- データファイル ---
BOOK_FILE = "books.json" # 本の管理データ
USER_FILE = "users.json" # ユーザー管理データ

# --- ユーティリティ ---
# データの読み込み処理
def load_data(filename):
    if os.path.exists(filename):
        try:
            with open(filename, "r", encoding="utf-8") as fileobj:
                return json.load(fileobj)

        except Exception:
            print("※ データが読み込めませんでした。")

    return {}

# データの書き込み(保存)処理
def save_data(filename, data):
    try:
        with open(filename, "w", encoding="utf-8") as fileobj:
            json.dump(data, fileobj)

    except Exception:
        print("※ データが保存できませんでした。")


#--- 管理者機能 ---
# 本の追加
def add_book(books):
    # 入力処理
    title = input("タイトル: ")
    author = input("著者名: ")

    # 未入力チェック
    if not title or not author:
        print("※ タイトルと著者名を入力してください。")
        return

    # 重複チェック
    if title in books:
        print("※ すでに登録されています。")
        return

    # 登録処理
    books[title] = {"author": author, "available": True}
    print("登録しました。")


# 本の検索
def search_books(books):
    # 検索キーワードの入力
    keyword = input("検索キーワード: ")

    # 未入力チェック
    if not keyword:
        print("※ キーワードを入力してください。")
        return

    # 検索処理
    for title, info in books.items():

        if keyword in title:

            # availableの表示テキストの置き換え
            status = "貸出中"
            if info["available"]:
                status = "貸出可"

            print(f"タイトル: {title}")
            print(f"著者名: {info["author"]}")
            print(f"状態: {status}")

        else:
            print("※ 該当する本が見つかりません。")

# 本の削除
def delete_book(books):
    # タイトルの入力
    title = input("削除するタイトル: ")

    # 本のチェック
    if title not in books:
        print("※ 該当する本が見つかりません。")
        return

    # 貸出中チェック
    if not books[title]["available"]:
        print("※ 貸出中で削除できません。")
        return

    # 削除処理
    del books[title]
    print("削除しました。")


# 本の更新
def update_book(books):
    # タイトルの入力
    title = input("更新するタイトル: ")

    # 本のチェック
    if title not in books:
        print("※ 該当する本が見つかりません。")
        return

    # 編集処理(著者名の編集)
    new_author = input("新しい著者名: ")

    # 未入力チェック
    if not new_author:
        print("※ 著者名を入力してください。")
        return
    
    # 更新処理
    books[title]["author"] = new_author
    print("更新しました。")

#--- ユーザー機能 ---
# ユーザー機能
# 本の貸出
def borrow_book(username, users, books):

    # 貸出数チェック
    if len(users[username]["borrowed"]) >= 3:
        print("※ 最大3冊までです。")
        return

    # 借りたい本のタイトルを入力
    title = input("借りたい本のタイトル: ")

    if title not in books:
        print("※ 該当する本が見つかりません。")
        return

    # 貸出中チェック
    if not books[title]["available"]:
        print("貸出中です。貸出できません。")
        return

    # 貸出処理
    books[title]["available"] = False
    users[username]["borrowed"].append(title)
    print("貸出しました。")
    
# 本の返却
def return_book(username, users, books):

    # 返却する本のタイトルの入力
    title = input("返却する本のタイトル: ")

    # 借りているかチェック
    if title not in users[username]["borrowed"]:
        print("※ その本は借りていません。")
        return

    # 返却処理
    books[title]["available"] = True
    users[username]["borrowed"].remove(title)
    print("返却しました。")

# 履歴確認
def show_history(username, users):

    # ユーザーの貸出履歴を取得
    borrowed = users[username]["borrowed"]
    if borrowed:
        print("借りている本: ")
        for id, title in enumerate(borrowed):
            print(f" {id+1}: {title}")
    
    else:
        print("借りている本はありません。")

# --- メニュー ---
# 管理者メニュー
def admin_menu():

    # 蔵書データの取得
    books = load_data(BOOK_FILE)

    while True:
        print("@管理者メニュー")
        print("1. 本を追加")
        print("2. 本を検索")
        print("3. 本を削除")
        print("4. 本を更新")
        print("5. 戻る")
        num = input("選択: [1-5]")

        if num == "1":
            print("本の追加")
            add_book(books)

        elif num == "2":
            print("本の検索")
            search_books(books)

        elif num == "3":
            print("本の削除")
            delete_book(books)
        
        elif num == "4":
            print("本の更新")
            update_book(books)

        elif num == "5":
            print("メインメニューへ戻る")
            break

        else:
            print("無効な選択です。")

        # データの保存
        save_data(BOOK_FILE, books)

# ユーザーメニュー
def user_menu():
    # ユーザーのデータの取得
    users = load_data(USER_FILE)

    # ユーザー登録
    username = input("ユーザー名: ")

    # 未入力チェック
    if not username:
        print("※ ユーザー名を入力してください。")
        return

    # ユーザーのチェック
    if username not in users:
        # 新規処理
        users[username] = {"borrowed":[]}
        print(f"{username}さん、新規ユーザー登録しました。")
    
    else:
        print(f"ようこそ、{username}さん!")

    while True:

        # 本のデータを取得
        books = load_data(BOOK_FILE)

        print(f"@ユーザー: [{username}]")
        print("1. 本を借りる")
        print("2. 本を返却する")
        print("3. 貸出履歴を見る")
        print("4. 戻る")
        num = input("選択: [1-4]")

        if num == "1":
            print("本を借りる")
            borrow_book(username, users, books)

        elif num == "2":
            print("本を返却する")
            return_book(username, users, books)

        elif num == "3":
            print("貸出履歴を見る")
            show_history(username, users)
        
        elif num == "4":
            print("メインメニューへ戻る")
            break

        else:
            print("無効な選択です。")

        # データの保存
        save_data(USER_FILE, users)

# メインメニュー
def main():
    while True:
        print("** 図書館システム **")

        ## メニュー
        print("1. 管理者モード")
        print("2. ユーザーモード")
        print("3. 終了")
        num = input("選択: [1-3]")

        if num == "1":
            admin_menu()
        
        elif num == "2":
            user_menu()
        
        elif num == "3":
            print("終了します。")
            break
        
        else:
            print("無効な選択です。")

# --- 実行処理 ---
if __name__ == "__main__":
    main()