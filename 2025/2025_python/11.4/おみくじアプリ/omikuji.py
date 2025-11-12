### omikuji.py
"""
おみくじアプリ
"""
# モジュール
import os # ファイルの存在確認に使用する
import random # 運勢をランダムに選ぶために使用する
from datetime import datetime # 日付の取得に使用する
import json # JSONファイルの読み書きに使用する

# ファイルの設定
DATA_FILE = "./11.4/おみくじアプリ/omikuzi_users.json"

# 運勢リスト
FORTUNES = ["大吉", "中吉", "小吉", "吉", "末吉", "凶"]

## 各関数の定義
# ユーザーのデータを読み込む
def load_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding  = "utf-8") as fileobj:
                data = json.load(fileobj) # JSON形式で読み込んで辞書型にする
                return data
        except:
            print("※ データファイルが破損、新しいファイルを作成します。")

    return {}

# 運勢を占う関数
def draw_fortune():
    fortune = random.choice(FORTUNES)
    return fortune # FORTUNESリストから1つ選択して返す

# ユーザーのデータをファイルに保存する関数
def save_data(data):
    try:
        with open(DATA_FILE, "w", encoding = "utf-8") as fileobj:
            # JSON形式でファイルに書き込む(保存)
            json.dump(data, fileobj, indent = 2, ensure_ascii = False)
    except:
        print("※ データの保存に失敗しました。")        

# メイン処理の関数
def main():
    print("--- おみくじアプリ ---")

    # 名前の入力(未入力または再入力を促す)
    while True:
        username = input("あなたの名前を入力してください:")

        if username:
            break
        
        print("※ 名前を入力してください。")

    # ユーザーの確認
    users = load_data()

    # 日付の取得(文字列形式)
    today = datetime.now().strftime("%Y-%m-%d")

    # 本日の利用確認(利用者の名前と日付を確認)
    if username in users and users[username]["date"] == today:
        # 利用履歴がある場合
        # 利用済みで結果を表示
        print(f"{username}さん、今日のおみくじはすでにひきました！")
        print(f"結果:{users[username]['fortune']} {users[username]['date']}")
    
    else:
        # 利用履歴がない場合
        # 新しく抽選して表示
        fortune = draw_fortune()

        # 結果を辞書型にしておく
        users[username] = {
            "fortune": fortune,
            "date": today
        }

        # 結果の表示
        print(f"{username}さんの今日の運勢は、{fortune}です！")

    # 結果を保存
    save_data(users)

# このファイルがスクリプトとして実行された場合のみmain()を呼び出す
if __name__ == "__main__":
    main()