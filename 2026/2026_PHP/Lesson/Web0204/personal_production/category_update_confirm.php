<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>更新確認</title>
</head>
<body>
    <h1>更新確認</h1>
    <form action="category_update.php" method="POST">
        <label>昔のカテゴリー名: <?php echo $_POST['category_old'], '<br>'; ?><input type="hidden" name="category_old" value="<?php echo $_POST['category_old']; ?>"></label>
        <label>新しいカテゴリー名: <?php echo $_POST['category_new'], '<br>'; ?><input type="hidden" name="category_new" value="<?php echo $_POST['category_new']; ?>"></label>
        <button type="submit" name="operation">更新</button>
    </form>
    <p><a href="category_update.html">戻る</a></p>
</body>
</html>
<script> 
    const btn = document.querySelector('button[type="submit"]') 
    btn.addEventListener('click', () => alert('更新しました。')); 
</script>