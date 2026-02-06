<?php
    declare(strict_types=1);

    require_once dirname(__FILE__) .'/db.php';
    
    try {
        if (!isset($_GET['title']) | trim($_GET['title']) === '') {
            return;
        }
        $pdo = connect();
        $statement = $pdo->prepare('INSERT INTO books(title, author) VALUES(:title, :author)');
        $statement->bindValue(':title', $_GET['title'], PDO::PARAM_STR);
        $statement->bindValue(':author', $_GET['author'], PDO::PARAM_STR);
        $statement->execute();
    } catch (PDOException $e) {
        echo '本の追加に失敗しました。';
        return;
    }
?>
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>テスト図書館</title>
</head>
<body>
    <h1>追加した本</h1>
    <table border="1">
        <tr>
            <th>タイトル</th>
            <th>著者</th>
        </tr>
            <tr>
                <td><?=escape($_GET['title']);?></td>
                <td><?=escape($_GET['author']);?></td>
            </tr>
    </table>
    <a href="./index.php">一覧ページに戻る</a>
</body>
</html>