<?php
    declare(strict_types=1);

    function connect(): PDO
    {
        $pdo = new PDO('mysql:host=localhost; dbname=honkaku; charset=utf8mb4', 'root', '');
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        $pdo->setAttribute(PDO::ATTR_EMULATE_PREPARES, false);
        return $pdo;
    }
?>
<body>
    <?php
        try {
            $pdo = connect();
            // $pdo->prepareメソッドでSQL実行前準備をする
            // 「:title, :price」値が入る場所を仮に確保→この場所のことをプレースホルダーという
            $statement = $pdo->prepare('INSERT INTO books(created, title, price) VALUES(CURRENT_TIMESTAMP, :title, :price)');
            // $statement->bindvalueメソッドでプレースホルダーに値を入れていく
            $statement->bindValue(':title', 'たのしいバドミントン', PDO::PARAM_STR);
            $statement->bindValue(':price', 820, PDO::PARAM_INT);
            // $statement->executeメソッドでバインドした結果のSQLを実行
            $statement->execute();
            $newId = $pdo->lastInsertId();
            echo '新しい本を登録しました。新しいレコードのIDは', $newId, 'です。';
        } catch (PDOException $e) {
            echo '新しい本の登録に失敗しました。';
        }
    ?>
</body>
