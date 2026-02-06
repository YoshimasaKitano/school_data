Readme.txt

## 実行手順

# 手順0
VScodeで開く場合、VScodeの以下の拡張機能をダウンロードしておく。
Python, Pylance

# 手順1
モジュールをインストールする。
pip install flask

pip install mysqlclient

pip install mysql

# 手順2
MySQL 8.0 Command Line Client - UnicodeでMySQLにログインして、デスクトップにコピーしたlws.sqlファイルを読み込む。
mysql> source C:\Users\cre\Desktop\lws.sql

lws.sqlファイルがない場合以下を順に実行してlwsデータベースとテーブルを作る。

drop database if exists lws_db;
create database lws_db;

use lws_db;

DROP TABLE IF EXISTS books;

DROP TABLE IF EXISTS users;

DROP TABLE IF EXISTS borrowings;

CREATE TABLE books (
    id INT AUTO_INCREMENT,
    title VARCHAR(255) UNIQUE NOT NULL,
    author VARCHAR(255) NOT NULL,
    available BOOLEAN NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE users (
    id INT AUTO_INCREMENT,
    username VARCHAR(255) UNIQUE NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE borrowings (
    id INT AUTO_INCREMENT,
    user_id INT,
    book_id INT,
    borrowed_at DATETIME NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (book_id) REFERENCES books(id)
);

COMMIT;

# 手順3
カレントディレクトリをKitano_Library_websystemまで変更し、app.pyを実行する。
py app.py

# 手順4
Webブラウザで起動する。
localhost:5000

## 機能

# 図書館管理システム
管理者モードとユーザーモードがある。
本の情報や、ユーザー情報をデータベースで管理している。
PCだけでなくスマホも対応。
エラーが起きるとindex.htmlにリダイレクトされます。


# 管理者モード
本の追加、本の検索、本の削除、本の更新、本の一覧表示が可能。

# 本の追加
データベースと接続して図書館に本を追加することができる。
タイトルと著者を入力して追加。

# 本の検索
データベースと接続して図書館にある本を検索することができる。
検索したいタイトルのキーワードを入力して、それが含まれているものを表示。

# 本の削除
データベースと接続して図書館にある本を削除することができる。
削除したいタイトルを入力して削除。

# 本の更新
データベースと接続して図書館にある本の著者を更新をすることができる。
更新したい著者の本のタイトルと更新した著者を入力して更新。

# 本の一覧表示
データベースと接続して図書館にある本の一覧を表示することができる。
ボタンを押すと検索して表示。


# ユーザーモード
ユーザー登録機能が搭載されている。
本の貸出、本の返却、本の一覧表示、履歴確認が可能

# 本の貸出
データベースと接続して図書館にある本を借りることができる。
借りたいタイトルを入力して貸出。

# 本の返却
データベースと接続して自分の借りている本を返却することができる。
返却したいタイトルを入力して返却。

# 本の一覧表示
データベースと接続して図書館にある本の一覧を表示することができる。
ボタンを押すと検索して表示。

# 履歴確認
データベースと接続して自分の借りている本の一覧を表示することができる。
ボタンを押すと検索して表示。