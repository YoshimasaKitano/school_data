<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>カテゴリー新規作成確認ページ</title>
    <link rel="stylesheet" href="static/css/reset.css">
    <link rel="stylesheet" href="static/css/style.css">
</head>
<body>
    <h1>カテゴリー新規作成確認ページ</h1>
    <form action="make_category.php" method="POST" enctype="multipart/form-data">
        <label>カテゴリー名: <?= $_POST['category']; ?><input type="hidden" name="category" value="<?= $_POST['category']; ?>" required></label><br>
        <button type="submit" name="operation">作成</button>
    </form>
    <p><a href="make_category.php">戻る</a></p>
</body>
</html>
<script> 
    const btn = document.querySelector('button[type="submit"]') 
    btn.addEventListener('click', () => alert('作成しました。')); 
</script>