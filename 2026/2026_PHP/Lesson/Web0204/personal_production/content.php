<?php 
    declare(strict_types=1); 
    require_once dirname(__FILE__) . '/functions.php';
?>
<?php
    try {
        $pdo = connect();
        $statement = $pdo->prepare('SELECT vocabulary, mean from notebooks WHERE category = :category');
        $statement->bindValue(':category', $_GET['content_operation'], PDO::PARAM_STR);
        $statement->execute();
    } catch (PDOException $e) {
        echo '検索に失敗しました。';
        return;
    }
    $rows = $statement->fetchall(PDO::FETCH_ASSOC);
?>
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>カテゴリーの中身一覧</title>
</head>
<body>
    <h1>カテゴリー中身一覧</h1>
    <table border="1">
        <tr>
            <th>単語名</th>
            <th>単語の意味</th>
        </tr>
        <?php foreach ($rows as $row): ?>
            <tr>
                <td><?=$row['vocabulary']; ?></td>
                <td><?=$row['mean']; ?></td>
            </tr>
        <?php endforeach; ?>
    </table>
    <p><a href="category.php">戻る</a></p>
</body>
</html>