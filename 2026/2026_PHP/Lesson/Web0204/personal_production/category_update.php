<?php 
    declare(strict_types=1); 
    require_once dirname(__FILE__) . '/functions.php';
?>
<?php
    if ($_SERVER['REQUEST_METHOD'] === 'POST') {
        try {
            $pdo = connect();
            $statement = $pdo->prepare('SELECT vocabulary FROM notebooks WHERE category = :category');
            $statement->bindValue(':category', $_POST['category_old'], PDO::PARAM_STR);
            $statement->execute();
        } catch (PDOException $e) {
            echo '検索に失敗しました。';
            return;
        }
        $rows = $statement->fetch(PDO::FETCH_ASSOC);
        foreach ($rows as $row) {
            try {
                $pdo = connect();
                $statement = $pdo->prepare('UPDATE notebooks SET category = :category WHERE vocabulary = :vocabulary');
                $statement->bindValue(':category', $_POST['category_new'], PDO::PARAM_STR);
                $statement->bindValue(':vocabulary', $row, PDO::PARAM_STR);
                $statement->execute();
            } catch (PDOException $e) {
                echo '更新に失敗しました。';
                return;
            }
        }
        header('Location: category.php');
    }
?>
<?php if ($_SERVER['REQUEST_METHOD'] === 'GET'): ?>
    <!DOCTYPE html>
        <html lang="ja">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>更新ページ</title>
        </head>
        <body>
            <h1>更新ページ</h1>
            <form action="category_update_confirm.php" method="POST">
                <label>元のカテゴリー名: <?=$_GET['category_update_operation']; ?><input type="hidden" name="category_old" value="<?=$_GET['category_update_operation']; ?>"></label><br>
                <label>新しいカテゴリー名: <input type="text" name="category_new"></label><br>
                <button type="submit" name="operation">更新</button>
            </form>
            <p><a href="category.php">戻る</a></p>
        </body>
    </html>
<?php endif; ?>