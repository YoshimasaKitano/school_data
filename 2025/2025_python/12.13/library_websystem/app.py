"""
図書館管理システム
"""
# モジュール
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import session
import MySQLdb
from config import DB_CONFIG

# Flask本体のインスタンスを生成
app = Flask(__name__)

app.secret_key = "library_key"

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
        count = 0
        try:
            conn = get_db_connection()
            print("DB接続成功")
            cursor = conn.cursor()
            sql = "SELECT * FROM books;"
            cursor.execute(sql, )
            emps = cursor.fetchall()
            for emp in emps:
                if title == emp[1]:
                    count += 1
                    return render_template('admin/add_confirm.html', count = count)

            else:
                return render_template('admin/add_confirm.html', title = title, author = author, count = count)
            
        except Exception as e:
            print("DB接続失敗")
            print("エラー内容",e)

            # return redirect('/')

        finally:
            conn.close()
            print("DB接続終了")
    
    # GET送信されてきた場合
    count = 0
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

            return redirect('/admin_menu')
        
        except Exception as e:
            print("DB接続失敗")
            print("エラー内容",e)

            # return redirect('/')

        finally:
            conn.close()
            print("DB接続終了")

# 本の検索の入力処理
@app.route('/search', methods=['GET', 'POST'])
def search():
        
        # POST送信されてきた場合
        if request.method == 'POST':
            keyword = request.form['keyword']

            try:
                conn = get_db_connection()
                print("DB接続成功")
                cursor = conn.cursor()
                sql = "SELECT title, author, available FROM books WHERE title LIKE %s;"
                cursor.execute(sql, ("%" + keyword + "%", ))
                emps = cursor.fetchall()
                return render_template('admin/search_result.html', emps = emps)

            except Exception as e:
                print("DB接続失敗")
                print("エラー内容",e)

            finally:
                conn.close()
                print("DB接続終了")
        
        # GET送信されてきた場合
        return render_template('admin/search.html')

# 本の削除の入力処理
@app.route('/delete', methods=['GET', 'POST'])
def delete():

    # POST送信されてきた場合の処理
    if request.method == 'POST':
        title = request.form['title']
        count = 0
        try:
            conn = get_db_connection()
            print("DB接続成功")
            cursor = conn.cursor()
            sql = "SELECT * FROM books;"
            cursor.execute(sql, )
            emps = cursor.fetchall()
            for emp in emps:
                if title in emp:
                    if emp[3] == 0:
                        count += 2
                        return render_template('admin/delete_confirm.html', count = count)
                    
                    count += 1
                    return render_template('admin/delete_confirm.html', title = title, count = count)
            
            if count == 0:
                return render_template('admin/delete_confirm.html', count = count)
            
        except Exception as e:
            print("DB接続失敗")
            print("エラー内容",e)

            # return redirect('/')

        finally:
            conn.close()
            print("DB接続終了")
    
    # GET送信されてきた場合
    count = 0
    return render_template('admin/delete.html')

# 本の削除の確認処理
@app.route('/delete_confirm', methods=['POST'])
def delete_confirm():
    if request.method == 'POST':
        title = request.form['title']

        try:
            conn = get_db_connection()
            print("DB接続成功")
            cursor = conn.cursor()
            sql = "DELETE FROM books WHERE title = %s;"
            cursor.execute(sql, (title, ))
            conn.commit()

            return redirect('/admin_menu')
        
        except Exception as e:
            print("DB接続失敗")
            print("エラー内容",e)

            # return redirect('/')

        finally:
            conn.close()
            print("DB接続終了")

# 本の更新の入力処理
@app.route('/update', methods=['GET', 'POST'])
def update():

    # POST送信されてきた場合の処理
    if request.method == 'POST':
        title = request.form['title']
        new_author = request.form['new_author']
        count = 0
        try:
            conn = get_db_connection()
            print("DB接続成功")
            cursor = conn.cursor()
            sql = "SELECT * FROM books;"
            cursor.execute(sql, )
            emps = cursor.fetchall()
            for emp in emps:
                if title == emp[1]:
                    count += 1
                    return render_template('admin/update_confirm.html', title = title, new_author = new_author,count = count)

            else:
                return render_template('admin/add_confirm.html', count = count)
            
        except Exception as e:
            print("DB接続失敗")
            print("エラー内容",e)

            # return redirect('/')

        finally:
            conn.close()
            print("DB接続終了")
    
    # GET送信されてきた場合
    count = 0
    return render_template('admin/update.html')

# 本の更新の確認処理
@app.route('/update_confirm', methods=['POST'])
def update_confirm():
    if request.method == 'POST':
        title = request.form['title']
        new_author = request.form['new_author']

        try:
            conn = get_db_connection()
            print("DB接続成功")
            cursor = conn.cursor()
            sql = "UPDATE books SET author=%s WHERE title=%s;"
            cursor.execute(sql, (new_author, title))
            conn.commit()

            return redirect('/admin_menu')
        
        except Exception as e:
            print("DB接続失敗")
            print("エラー内容",e)

            # return redirect('/')

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
                cursor = conn.cursor()
                sql = "INSERT INTO users (username) VALUES (%s);"
                cursor.execute(sql, (name, ))
                conn.commit()

                sql = "SELECT id FROM users WHERE username = %s;"
                cursor.execute(sql, (name, ))
                emp = cursor.fetchone()
                session['user_id'] = emp[0]

                return redirect('/user_menu')
            else:
                sql = "SELECT id FROM users WHERE username = %s;"
                cursor.execute(sql, (name, ))
                emp = cursor.fetchone()
                session['user_id'] = emp[0]
                return redirect('/user_menu')

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

# 本の貸出入力処理
@app.route('/borrow', methods=['GET', 'POST'])
def borrow():

    # POST送信されてきた場合の処理
    if request.method == 'POST':
        title = request.form['title']
        count = 0
        try:
            conn = get_db_connection()
            print("DB接続成功")
            cursor = conn.cursor()
            sql = "SELECT * from books;"
            cursor.execute(sql, )
            emps = cursor.fetchall()
            for emp in emps:
                if title == emp[1]:
                    if emp[3] == 0:
                        count += 2
                        return render_template('user/borrow_confirm.html', title = title, count = count)
                    count += 1
                    return render_template('user/borrow_confirm.html', title = title, count = count)

            else:
                return render_template('user/borrow_confirm.html', count = count)
            
        except Exception as e:
            print("DB接続失敗")
            print("エラー内容",e)

        # return redirect('/')

        finally:
            conn.close()
            print("DB接続終了")

    # GET送信されてきた場合
    count = 0
    user_id = session.get('user_id')
    try:
        conn = get_db_connection()
        print("DB接続成功")
        cursor = conn.cursor()
        sql = "SELECT username FROM users WHERE id = %s;"
        cursor.execute(sql, (user_id, ))
        name = cursor.fetchone()
        sql = "SELECT book_id FROM borrowings JOIN users ON borrowings.user_id = users.id WHERE users.username = %s;"
        cursor.execute(sql, (name[0], ))
        emps = cursor.fetchall()
        if len(emps) == 3:
            count += 1
            return render_template('user/borrow.html', count = count)
        
        else:
            return render_template('user/borrow.html')

    except Exception as e:
        print("DB接続失敗")
        print("エラー内容",e)

    # return redirect('/')

    finally:
        conn.close()
        print("DB接続終了")

# 本の貸出確認処理
@app.route('/borrow_confirm', methods=['POST'])
def borrow_confirm():
    if request.method == 'POST':
        title = request.form['title']
        user_id = session.get('user_id')

        try:
            conn = get_db_connection()
            print("DB接続成功")
            cursor = conn.cursor()
            sql = "UPDATE books SET available=0 WHERE title=%s;"
            cursor.execute(sql, (title, ))
            conn.commit()

            sql = "SELECT id FROM books WHERE title=%s;"
            cursor.execute(sql, (title, ))
            book_id = cursor.fetchone()

            sql = "INSERT INTO borrowings (user_id, book_id, borrowed_at) VALUES (%s, %s, NOW());"
            cursor.execute(sql, (user_id, book_id, ))
            conn.commit()

            return redirect('/user_menu')
        
        except Exception as e:
            print("DB接続失敗")
            print("エラー内容",e)

            # return redirect('/')

        finally:
            conn.close()
            print("DB接続終了")

# 本の返却の入力処理
@app.route('/return', methods=['GET', 'POST'])
def return_():

    # POST送信されてきた場合の処理
    if request.method == 'POST':
        title = request.form['title']
        count = 0
        try:
            conn = get_db_connection()
            print("DB接続成功")
            cursor = conn.cursor()
            sql = "SELECT id from books WHERE title=%s;"
            cursor.execute(sql, (title, ))
            book_id = cursor.fetchone()

            sql = "SELECT * from borrowings;"
            cursor.execute(sql, )
            emps = cursor.fetchall()
            print(emps)
            print(book_id)
            for emp in emps:
                if book_id[0] == emp[2]:
                    count += 1
                    return render_template('user/return_confirm.html', title = title, count = count)

            else:
                return render_template('user/return_confirm.html', count = count)
            
        except Exception as e:
            print("DB接続失敗")
            print("エラー内容",e)

        # return redirect('/')

        finally:
            conn.close()
            print("DB接続終了")

    # GET送信されてきた場合
    count = 0
    return render_template('/user/return.html')

# 本の返却確認処理
@app.route('/return_confirm', methods=['POST'])
def return_confirm():
    if request.method == 'POST':
        title = request.form['title']

        try:
            conn = get_db_connection()
            print("DB接続成功")
            cursor = conn.cursor()
            sql = "UPDATE books SET available=1 WHERE title=%s;"
            cursor.execute(sql, (title, ))
            conn.commit()

            sql = "SELECT id FROM books WHERE title=%s;"
            cursor.execute(sql, (title, ))
            book_id = cursor.fetchone()

            sql = "DELETE FROM borrowings WHERE book_id=%s;"
            cursor.execute(sql, (book_id, ))
            conn.commit()

            return redirect('/user_menu')
        
        except Exception as e:
            print("DB接続失敗")
            print("エラー内容",e)

            # return redirect('/')

        finally:
            conn.close()
            print("DB接続終了")

# 履歴確認処理
@app.route('/history')
def history():
    emps = []
    user_id = session.get('user_id')
    try:
        conn = get_db_connection()
        print("DB接続成功")
        cursor = conn.cursor()
        sql = "SELECT book_id FROM borrowings WHERE user_id=%s;"
        cursor.execute(sql, (user_id, ))
        book_ids = cursor.fetchall()
        for book_id in book_ids:
            sql = "SELECT title FROM books WHERE id=%s;"
            cursor.execute(sql, (book_id[0], ))
            emps.append(cursor.fetchone())
        return render_template('/user/history.html', emps = emps)
    
    except Exception as e:
        print("DB接続失敗")
        print("エラー内容", e)
    
    finally:
        conn.close()
        print("DB接続終了")

if __name__ == "__main__":
    app.run(debug=True)