<?php
    declare(strict_types=1);

    require_once dirname(__FILE__) .'/db.php';

    try {
        $pdo = connect();
        $statement = $pdo->prepare('SELECT * FROM books');
        $statement->execute();
    } catch (PDOException $e) {
        echo '本の検索に失敗しました。';
        return;
    }
?>
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>フォーム</title>
</head>
<body>
    <h1>現在の本一覧</h1>
        <table border="1">
            <tr>
                <th>書籍ID</th>
                <th>タイトル</th>
                <th>著者</th>
                <th>貸出可能か</th>
            </tr>
            <?php while ($row = $statement->fetch(PDO::FETCH_ASSOC)): ?>
                <tr>
                    <td><?=$row['id'];?></td>
                    <td><?=escape($row['title']);?></td>
                    <td><?=escape($row['author']);?></td>
                    <td>
                        <?php if ($row['available'] == 1) {
                            echo '貸出可';
                        } else {
                            echo '貸出不可';
                        }
                        ?>
                    </td>
                </tr>
            <?php endwhile; ?>
        </table>
    <h2>タイトルと著者で登録</h2>
    <form action="form.php" methods="GET">
        <p>タイトル：<input type="text" name="title" required></p>
        <p>著者：<input type="text" name="author" required></p>
        <button type="submit" value="登録">登録</button>
    </form>
</body>
</html>