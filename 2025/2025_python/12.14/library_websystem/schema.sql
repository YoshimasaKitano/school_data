-- lws_dbの作成
drop database if exists lws_db;
create database lws_db;

-- lws_dbを使用
use lws_db;

-- booksテーブルの削除
DROP TABLE IF EXISTS books;

-- usersテーブルの削除
DROP TABLE IF EXISTS users;

-- borrowingsテーブルの削除
DROP TABLE IF EXISTS borrowings;

-- booksテーブルの作成
CREATE TABLE books (
    id INT AUTO_INCREMENT,
    title VARCHAR(255) UNIQUE NOT NULL,
    author VARCHAR(255) NOT NULL,
    available BOOLEAN NOT NULL,
    PRIMARY KEY(id)
);

-- usersテーブルの作成
CREATE TABLE users (
    id INT AUTO_INCREMENT,
    username VARCHAR(255) UNIQUE NOT NULL,
    PRIMARY KEY(id)
);

-- borrowingsテーブルの作成
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



