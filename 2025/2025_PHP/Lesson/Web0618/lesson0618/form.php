<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>入力フォーム</title>
</head>
<body>
    <h2>入力フォーム</h2>
    <form action ="" method="POST">
        <p><label>名前：</label><input type="text" name="name" id="name"></p>
        <p><input type="submit" value="送信"></p>
    </form>

    <p>入力内容</p>
    名前: <?php echo $_POST['name']; ?>
</body>
</html>