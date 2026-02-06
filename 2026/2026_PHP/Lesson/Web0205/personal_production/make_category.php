<?php 
    declare(strict_types=1); 
    require_once dirname(__FILE__) . '/functions.php';
?>
<?php
    if ($_SERVER['REQUEST_METHOD'] === 'POST') {
        session_start();
        if (!empty($categories)) {
            $categories[] = $_POST['category'];
            $categories = array_adjust($categories);
            $_SESSION['category'] = $categories;
        } else {
            $categories = $_SESSION['category'];
            $categories[] = $_POST['category'];
            $categories = array_adjust($categories);
            $_SESSION['category'] = $categories;
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
        <title>カテゴリー新規作成</title>
        <link rel="stylesheet" href="static/css/reset.css">
        <link rel="stylesheet" href="static/css/style.css">
    </head>
    <body>
        <h1>カテゴリー新規作成</h1>
        <form action="make_category_confirm.php" method="POST" enctype="multipart/form-data">
            <label>カテゴリー名: <input type="text" name="category" required></label><br>
            <button type="submit" name="operation">作成</button>
        </form>
    </body>
    </html>
    <p><a href="category.php">戻る</a></p>
<?php endif; ?>