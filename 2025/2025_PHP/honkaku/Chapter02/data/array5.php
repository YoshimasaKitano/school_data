<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello World - honkaku</title>
    <title></title>
</head>
<body>
    <?php
        $userData = [12345, 'Tarou Yamada', 'Tokyo', 32];
        list($id, $name, $prefecture, $age) = $userData;
    ?>
    <p>ユーザID：<?=$id?></p>
    <p>ユーザ名：<?=$name?></p>
    <p>都道府県：<?=$prefecture?></p>
    <p>年齢：<?=$age?></p>
</body>
</html>