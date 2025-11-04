<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <form action="" method="POST">
        <label>名前：</label><input type="text" name="name">
        <input type="submit" value="送信">
    </form>
 <?php if (empty($_POST['name'])) {
                echo 'ユーザー名を入力してください。';
            } else {
                echo htmlspecialchars($_POST['name'], ENT_QUOTES, 'UTF-8');
            }
    // <?= htmlspecialchars($_POST['name'], ENT_QUOTES, 'UTF-8'); ?>
</body>
</html>