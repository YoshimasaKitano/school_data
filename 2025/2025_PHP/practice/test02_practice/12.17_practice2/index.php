<?php
    declare(strict_types=1);

    require_once dirname(__FILE__) .'/db.php';

    try {
        $pdo = connect();
        $statement = $pdo->prepare('SELECT * FROM users');
        $statement->execute();
    } catch (PDOException $e) {
        echo '検索に失敗しました。';
        return;
    }
?>
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ユーザー登録</title>
</head>
<body>
    <h1>[ ユーザー登録フォーム ]</h1>
    <form action="/form.php">
        <ul>
            <li>
                <p>名前：</p>
            </li>
            <li>
                <input type="text" name="name" required>
            </li>
        </ul>
        <ul>
            <li>
                <p>メール：</p>
            </li>
            <li>
                <input type="text" name="email" required>
            </li>
        </ul>
        <button type="submit">[ 登録 ]</button>
    </form>
    <h2>[ ユーザー検索 ]</h2>
    <form action="/form.php">
        <ul>
            <li>
                <p>名前：</p>
            </li>
            <li>
                <input type="text" name="name" required>
            </li>
        </ul>
        <button type="submit">[ 検索 ]</button>
    </form>
    <h2>[ ユーザー一覧 ]</h2>
    <table border="1">
        <tr>
            <th>ID</th>
            <th>名前</th>
            <th>メール</th>
            <th>登録日時</th>
        </tr>
        <?php while ($row = $statement->fetch(PDO::FETCH_ASSOC)): ?>
            <tr>
                <td><?=$row['id'];?></td>
                <td><?=escape($row['title']); ?></td>
                <td><?=escape($row['email']); ?></td>
                <td><?=$row['created_at']; ?></td>
            </tr>
        <?php endwhile; ?>
    </table>
</body>
</html>