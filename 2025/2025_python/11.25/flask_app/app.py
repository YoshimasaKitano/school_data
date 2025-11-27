# app.py
from flask import Flask # Flask本体のインポート
from flask import render_template # htmlのテンプレートを表示するためのモジュール
from flask import request # リクエスト情報を取得するモジュール

# データベース接続のモジュール
import MySQLdb
from config import DB_CONFIG

app = Flask(__name__) # Flask本体からインスタンスを生成

# データベース接続の関数
def get_db_connection():
    return MySQLdb.connect(**DB_CONFIG)

## 各関数の定義
# 従業員一覧
@app.route("/employee-list.html", methods=["GET"])
def employee_list():

    conn = get_db_connection()
    cursor = conn.cursor()
    sql = "select * from employee;"
    cursor.execute(sql,)
    emps = cursor.fetchall()
    conn.close()

    params = {
        "title": "従業員一覧",
        "msg": "従業員情報を一覧表示します。",
        "emps": emps
    }

    return render_template("employee-list.html", **params)

# ルーティングの処理(コントローラーの役割)
# index処理の関数
@app.route("/") # :5000の後のスラッシュ(何も指定がなかった場合これが実行される)
def index():
    # 辞書型でパラメータで設定
    params = {
        "title":"Flask App",
        "msg":"ここは、index ページです。"
    }

    return render_template("index.html", **params) # 可変長で入れるために**

# form処理の関数
@app.route("/form.html", methods=["GET","POST"])
def form():
    text = ""
    if request.method == "GET": # GET送信されてきた場合
        text = "ここは、form ページです。"

    elif request.method == "POST": # POST送信されてきた場合
        text = request.form["text"]

    params = {
        "title":"Flask App",
        "msg":text
    }

    return render_template("form.html", **params)
    
# @app.route("/form.html",methods=["GET"])
# def form():
#     params = {
#         "title":"Flask App",
#         "msg":"ここは、form ページです。"
#     }
#     return render_template("form.html", **params)

# @app.route("/form.html",methods=["POST"])
# def form():
#     # リクエストパラメータの取得
#     text = request.form["text"]

#     params = {
#         "title":"Flask App",
#         "msg":text;
#     }

#     return render_template("form.html", **params)

# def hello():
#     return "Hello Flask app"

# Flaskアプリの呼び出しと実行の処理→エントリーポイント
if __name__ == "__main__":
    app.run(debug=True)


