<?php 
    declare(strict_types=1); 
    require_once dirname(__FILE__) . '/functions.php';
?>
<?php
    if ($_SERVER['REQUEST_METHOD'] === 'POST') {
        try {
            $pdo = connect();
            $statement = $pdo->prepare('SELECT mean, category FROM notebooks WHERE vocabulary = :vocabulary');
            $statement->bindValue(':vocabulary', $_POST['vocabulary'], PDO::PARAM_STR);
            $statement->execute();
        } catch (PDOException $e) {
            echo '検索に失敗しました。';
            return;
        }
        $rows =  $statement->fetch(PDO::FETCH_ASSOC);
        $mean = $rows['mean'];
        $category = $rows['category'];
    }
?>
<?php if ($_POST['mean'] == ''): ?>
    <!DOCTYPE html>
    <html lang="ja">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>更新確認</title>
        <link rel="stylesheet" href="static/css/reset.css">
        <link rel="stylesheet" href="static/css/style.css">
    </head>
    <body>
        <h1>更新確認</h1>
        <form action="update.php" method="POST">
            <label>単語: <?= $_POST['vocabulary'], '<br>'; ?><input type="hidden" name="vocabulary" value="<?= $_POST['vocabulary']; ?>"></label>
            <label>意味(変更なし): <?= $mean, '<br>';?><input type="hidden" name="mean" value="<?= $_POST['mean']; ?>"></label>
            <label>カテゴリー: <?= $_POST['category'], '<br>'; ?><input type="hidden" name="category" value="<?= $_POST['category']; ?>"></label>
            <button type="submit" name="operation">更新</button>
        </form>
        <p><a href="search.php">戻る</a></p>
    </body>
    </html>
    <script> 
        const btn = document.querySelector('button[type="submit"]') 
        btn.addEventListener('click', () => alert('更新しました。')); 
    </script>
<?php elseif ($_POST['category'] == ''): ?>
    <!DOCTYPE html>
    <html lang="ja">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>更新確認</title>
        <link rel="stylesheet" href="static/css/reset.css">
        <link rel="stylesheet" href="static/css/style.css">
    </head>
    <body>
        <h1>更新確認</h1>
        <form action="update.php" method="POST">
            <label>単語: <?= $_POST['vocabulary'], '<br>'; ?><input type="hidden" name="vocabulary" value="<?= $_POST['vocabulary']; ?>"></label>
            <label>意味: <?= $_POST['mean'], '<br>';?><input type="hidden" name="mean" value="<?= $_POST['mean']; ?>"></label>
            <label>カテゴリー(変更なし): <?= $category, '<br>'; ?><input type="hidden" name="category" value="<?= $_POST['category']; ?>"></label>
            <button type="submit" name="operation">更新</button>
        </form>
        <p><a href="search.php">戻る</a></p>
    </body>
    </html>
    <script> 
        const btn = document.querySelector('button[type="submit"]') 
        btn.addEventListener('click', () => alert('更新しました。')); 
    </script>
<?php else: ?>
    <!DOCTYPE html>
    <html lang="ja">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>更新確認</title>
        <link rel="stylesheet" href="static/css/reset.css">
        <link rel="stylesheet" href="static/css/style.css">
    </head>
    <body>
        <h1>更新確認</h1>
        <form action="update.php" method="POST">
            <label>単語: <?= $_POST['vocabulary'], '<br>'; ?><input type="hidden" name="vocabulary" value="<?= $_POST['vocabulary']; ?>"></label>
            <label>意味: <?= $_POST['mean'], '<br>';?><input type="hidden" name="mean" value="<?= $_POST['mean']; ?>"></label>
            <label>カテゴリー: <?= $_POST['category'], '<br>'; ?><input type="hidden" name="category" value="<?= $_POST['category']; ?>"></label>
            <button type="submit" name="operation">更新</button>
        </form>
        <p><a href="search.php">戻る</a></p>
    </body>
    </html>
    <script> 
        const btn = document.querySelector('button[type="submit"]') 
        btn.addEventListener('click', () => alert('更新しました。')); 
    </script>
<?php endif; ?>