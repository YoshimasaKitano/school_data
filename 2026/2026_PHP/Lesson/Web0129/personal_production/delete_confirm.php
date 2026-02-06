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
            if ($_GET['delete_operation'] == $i) {
                try {
                    $pdo = connect();
                    $statement = $pdo->prepare('SELECT vocabulary, mean, category FROM notebooks WHERE index_number = :index_number');
                    $statement->bindValue(':index_number',$i, PDO::PARAM_INT);
                    $statement->execute();
                } catch (PDOException $e) {
                    echo '単語の検索に失敗しました。';
                    return;
                }
                $row = $statement->fetch(PDO::FETCH_ASSOC);
                $vocabulary = $row['vocabulary'];
                $mean = $row['mean'];
                $category = $row['category'];
            }
        }
    }
?>
    <!DOCTYPE html>
    <html lang="ja">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>削除確認</title>
    </head>
    <body>
        <h1>削除確認</h1>
        <form action="delete.php" method="POST">
            <label>単語: <?php echo $vocabulary, '<br>'; ?><input type="hidden" name="vocabulary" value="<?php echo $vocabulary; ?>"></label>
            <label>意味: <?php echo $mean, '<br>';?><input type="hidden" name="mean" value="<?php echo $mean; ?>"></label>
            <label>カテゴリー: <?php echo $category, '<br>'; ?><input type="hidden" name="category" value="<?php echo $category; ?>"></label>
            <button type="submit" name="operation">削除</button>
        </form>
        <p><a href="search.php">戻る</a></p>
    </body>
    </html>
    <script> 
        const btn = document.querySelector('button[type="submit"]') 
        btn.addEventListener('click', () => alert('削除しました。')); 
    </script>