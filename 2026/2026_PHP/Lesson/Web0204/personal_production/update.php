<?php declare(strict_types=1); ?>

<?php
    require_once dirname(__FILE__) . '/functions.php';

    if ($_SERVER['REQUEST_METHOD'] === 'GET') {
        try{
            $pdo = connect();
            $statement = $pdo->prepare('SELECT * FROM notebooks');
            $statement->execute();
        } catch (PDOException $e) {
            echo '検索に失敗しました。';
            return;
        }
        $row_count = count($statement->fetchall(PDO::FETCH_ASSOC));
        for ($i = 0; $i < $row_count; $i++) {
            if ($_GET['update_operation'] == $i) {
                try {
                    $pdo = connect();
                    $statement = $pdo->prepare('SELECT vocabulary FROM notebooks WHERE index_number = :index_number');
                    $statement->bindValue(':index_number',$i, PDO::PARAM_INT);
                    $statement->execute();
                } catch (PDOException $e) {
                    echo '単語の検索に失敗しました。';
                    return;
                }
                $row = $statement->fetch(PDO::FETCH_ASSOC);
                $vocabulary = $row['vocabulary'];
            }
        }
    } else {
        if ($_POST['category'] == '') {
            $_POST['category'] = NULL;
        }
        try {
            $pdo = connect();
            $statement = $pdo->prepare('UPDATE notebooks SET mean = :mean, category = :category WHERE vocabulary = :vocabulary');
            $statement->bindValue(':mean', $_POST['mean'], PDO::PARAM_STR);
            $statement->bindValue(':category', $_POST['category'], PDO::PARAM_STR);
            $statement->bindValue(':vocabulary', $_POST['vocabulary'], PDO::PARAM_STR);
            $statement->execute();
        } catch (PDOException $e) {
            echo '更新に失敗しました。';
            return;
        }
        header('Location: search.php');
    }
?>
<?php if ($_SERVER['REQUEST_METHOD'] == 'GET'): ?>
    <!DOCTYPE html>
    <html lang="ja">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>更新確認</title>
    </head>
    <body>
        <h1>更新ページ</h1>
        <form action="update_confirm.php" method="POST">
            <label>単語: <?php echo $vocabulary, '<br>'; ?><input type="hidden" name="vocabulary" value="<?php echo $vocabulary; ?>"></label>
            <label>意味: <input type="text" name="mean" required></label><br>
            <label>カテゴリー: <input type="text" name="category"></label><br>
            <button type="submit" name="operation">更新</button>
        </form>
        <p><a href="search.php">戻る</a></p>
    </body>
    </html>
<?php endif; ?>