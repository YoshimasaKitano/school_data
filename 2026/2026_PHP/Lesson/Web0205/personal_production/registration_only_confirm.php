<?php if ($_GET['category'] == '') {
    $_GET['category'] == NULL;
}
?>
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>単語の単一登録</title>
    <link rel="stylesheet" href="static/css/reset.css">
    <link rel="stylesheet" href="static/css/style.css">
</head>
<body>
    <h1>登録確認</h1>
    <form action="registration_only.php" method="POST">
        <label>単語: <?= $_GET['vocabulary'], '<br>'; ?><input type="hidden" name="vocabulary" value="<?= $_GET['vocabulary']; ?>"></label>
        <label>意味: <?= $_GET['mean'], '<br>'; ?><input type="hidden" name="mean" value="<?= $_GET['mean']; ?>"></label>
        <label>カテゴリー: <?= $_GET['category'], '<br>'; ?><input type="hidden" name="category" value="<?= $_GET['category']; ?>"></label>
        <button type="submit" name="operation">登録</button>
    </form>
    <p><a href="registration_only.php">戻る</a></p>
</body>
</html>
<script> 
    const btn = document.querySelector('button[type="submit"]') 
    btn.addEventListener('click', () => alert('登録しました。')); 
</script>