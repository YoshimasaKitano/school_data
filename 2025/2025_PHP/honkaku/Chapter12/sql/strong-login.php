<?php
    // DBに接続する関数
    function connect(): PDO
    {
        $pdo = new PDO('mysql:host=localhost; dbname=honkaku; charset=utf8mb4', 'root', '');
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        $pdo->setAttribute(PDO::ATTR_EMULATE_PREPARES, false);
        return $pdo;
    }

    // ログインID・パスワードを元に一致するユーザを探す関数
    function findUser(string $loginId, string $password): ?array
    {
        $pdo = connect();
        $sql = "SELECT * FROM honkaku_users WHERE login_id = :login_id AND password =:password";
        $statement = $pdo->prepare($sql);
        $statement->bindValue(':login_id', $loginId, PDO::PARAM_STR);
        $statement->bindValue(':password', $password, PDO::PARAM_STR);
        $statement->execute();
        $users = $statement->fetchAll(PDO::FETCH_ASSOC);
        if (count($users) === 1) {
            return $users[0];
        }
        return null;
    }