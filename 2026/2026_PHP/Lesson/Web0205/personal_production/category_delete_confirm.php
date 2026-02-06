<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>削除確認</title>
    <link rel="stylesheet" href="static/css/reset.css">
    <link rel="stylesheet" href="static/css/style.css">
</head>
<body>
    <h1>削除確認</h1>
    <form action="category_delete.php" method="POST">
        <label>削除するカテゴリー: <?=$_GET['category_delete_operation'], '<br>'; ?><input type="hidden" name="category" value="<?=$_GET['category_delete_operation']; ?>"></label>
        <button type="submit" name="operation">削除</button>
    </form>
    <p><a href="category.php">戻る</a></p>
</body>
</html>
<script>
    const btn = document.querySelector('button[type="submit"]')
    btn.addEventListener('click', () => alert('削除しました。')); 
</script>