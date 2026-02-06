<?php declare(strict_types=1); ?>

<?php
    require_once dirname(__FILE__) . '/functions.php';

    if ($_SERVER['REQUEST_METHOD'] === 'GET') {
        
    }


<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>単語の単一登録</title>
</head>
<body>
    <h1>削除確認</h1>
    <form action="registration_only.php" method="POST">
        <p>単語:<input type="text" name="vocabulary" value="<?php echo $_GET['vocabulary']; ?>"></p>
        <p>意味:<input type="text" name="mean" value="<?php echo $_GET['mean']; ?>"></p>
        <p>カテゴリー:<input type="text" name="category" value="<?php echo $_GET['category']; ?>"></p>
        <button type="submit" name="operation">削除</button>
    </form>
</body>
</html>
<script> 
    const btn = document.querySelector('button[type="submit"]') 
    btn.addEventListener('click', () => alert('登録しました。')); 
</script>