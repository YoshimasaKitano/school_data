### app.py
"""
エントリーポイントとコントローラーの役目
"""
# モジュールのインポート
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
# 従業員一覧処理
@app.route('/')
def index():
    try:
        conn = get_db_connection()
        print("DB接続成功")
        cursor = conn.cursor()
        sql = "select employee_no,employee_name,password from employee;"
        cursor.execute(sql)
        emps = cursor.fetchall()
        return render_template('index.html',emps = emps)

    except Exception as e:
        print("DB接続失敗")
        print("エラー内容",e)

    finally:
        conn.close()
        print("DB接続終了")

# 新規登録処理
## 入力画面
@app.route('/create',methods=['GET','POST'])
def create():
    if request.method == 'POST':
        no = request.form['no']
        name = request.form['name']
        password = request.form['password']
        return render_template('create_confirm.html', no=no,name=name,password=password)
    return render_template('create.html')

## 登録処理
@app.route('/create_confirm', methods=['POST'])
def create_confirm():
    if request.method == 'POST':
        no = request.form['no']
        name = request.form['name']
        password = request.form['password']

        try:
            conn = get_db_connection()
            print("DB接続成功")
            cursor = conn.cursor()
            sql = "INSERT INTO employee (employee_no, employee_name, password) VALUES (%s, %s, %s)"
            cursor.execute(sql, (no, name, password))
            conn.commit()

            return redirect('/')

        except Exception as e:
            print("DB接続失敗")
            print("エラー内容",e)

        finally:
            conn.close()
            print("DB接続終了")


# 更新処理
## 編集処理
@app.route('/edit/<id>', methods=['GET','POST'])
def edit(id):

    try:
        conn = get_db_connection()
        print("DB接続成功")
        cursor = conn.cursor()

        if request.method == 'POST':
            no = request.form['no']
            name = request.form['name']
            password = request.form['password']

            return render_template('edit_confirm.html', no=no,name=name,password=password)

        sql = "SELECT * FROM employee WHERE employee_no=%s;"
        cursor.execute(sql,(id,))
        emp = cursor.fetchone()
        return render_template('edit.html', no=emp[0],name=emp[1],password=emp[2])

    except Exception as e:
        print("DB接続失敗")
        print("エラー内容",e)

    finally:
        conn.close()
        print("DB接続終了")



# 実行処理
if __name__ == '__main__':
    app.run(debug=True)




