"""
図書館管理システム
"""
# モジュール
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
import MySQLdb
from config import DB_CONFIG

# Flask本体のインスタンスを生成
app = Flask(__name__)

# データベース接続関数
def get_db_connection():
    return MySQLdb.connect(**DB_CONFIG)

## 各関数の定義
# トップページのモード選択
@app.route('/')
def index():
    return render_template('index.html')

## 管理者モードの処理
# 管理者画面を表示する処理
@app.route('/admin_menu')
def admin_menu():
    return render_template('admin/admin_menu.html')

# 本の追加の入力処理
@app.route('/add', methods=['GET', 'POST'])
def add():

    # POST送信されてきた場合の処理
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        return render_template('admin/add_confirm.html', title = title, author = author)
    
    # GET送信されてきた場合
    return render_template('admin/add.html')
    
# 本の追加の確認処理
@app.route('/add_confirm', methods=['POST'])
def add_confirm():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']

        try:
            conn = get_db_connection()
            print("DB接続成功")
            cursor = conn.cursor()
            sql = "INSERT INTO books (title, author, available) VALUES (%s, %s, true);"
            cursor.execute(sql, (title, author))
            conn.commit()

            return redirect('/')
        
        except Exception as e:
            print("DB接続失敗")
            print("エラー内容",e)

            # return redirect('/')

        finally:
            conn.close()
            print("DB接続終了")

# 本の検索の入力処理
@app.route('/search', methods=['POST'])
def search():
        
        keyword = request.form['keyword']

        try:
            conn = get_db_connection()
            print("DB接続成功")
            cursor = conn.cursor()
            sql = "select (title, author, available) from books where title like %s;"
            cursor.execute(sql, ("%" + keyword + "%", ))
            emps = cursor.fetchall()
            return render_template('admin/search_result.html', emps = emps)

        except Exception as e:
            print("DB接続失敗")
            print("エラー内容",e)

        finally:
            conn.close()
            print("DB接続終了")

## ユーザーモードの処理
# ユーザー登録の処理
@app.route('/user', methods=['GET', 'POST'])
def user():
    
    # POST送信されてきたらパラメータを使って検索する処理
    if request.method == 'POST':
        name = request.form['name']

        try:
            conn = get_db_connection()
            print("DB接続成功")
            cursor = conn.cursor()
            sql = "select * from users where username like %s;"
            cursor.execute(sql, (name, ))
            emps = cursor.fetchall()

            if not emps:
                print("a")
                cursor = conn.cursor()
                sql = "INSERT INTO users (username) VALUES (%s);"
                cursor.execute(sql, (name))
                conn.commit()

                return redirect('/user_menu')
            else:
                return render_template('user/user_menu.html', emps = emps)

        except Exception as e:
            print("DB接続失敗")
            print("エラー内容",e)

        finally:
            conn.close()
            print("DB接続終了")
    
    return render_template('user/user.html')

# ユーザー画面を表示する処理
@app.route('/user_menu')
def user_menu():
    return render_template('user/user_menu.html')

#
if __name__ == "__main__":
    app.run(debug=True)