<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>更新確認</title>
</head>
<body>
    <h1>更新確認</h1>
    <form action="update.php" method="POST">
        <label>単語: <?php echo $_POST['vocabulary'], '<br>'; ?><input type="hidden" name="vocabulary" value="<?php echo $_POST['vocabulary']; ?>"></label>
        <label>意味: <?php echo $_POST['mean'], '<br>';?><input type="hidden" name="mean" value="<?php echo $_POST['mean']; ?>"></label>
        <label>カテゴリー: <?php echo $_POST['category'], '<br>'; ?><input type="hidden" name="category" value="<?php echo $_POST['category']; ?>"></label>
        <button type="submit" name="operation">更新</button>
    </form>
    <p><a href="search.php">戻る</a></p>
</body>
</html>
<script> 
    const btn = document.querySelector('button[type="submit"]') 
    btn.addEventListener('click', () => alert('更新しました。')); 
</script>