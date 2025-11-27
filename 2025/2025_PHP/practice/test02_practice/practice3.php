<?php
    try {
        $pdo = new PDO('mysql: host=localhost; dbname=honkaku; charset=utf8mb4', 'root', '');

        $pdo->setAttribute(ATTR_ERRMODE, ATTR_ERRMODE_EXCEPTION);
        $pdo->setAttribute(ATTR_EMULATE_PREPARES, false);
        echo '接続に成功しました。';
    } catch (PDOException $e) {
        echo '接続に失敗しました。';
    }
?>