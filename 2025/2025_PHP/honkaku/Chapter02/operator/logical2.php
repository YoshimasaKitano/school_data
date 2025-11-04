<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php
        // 以下のコメントを外すと、出力結果はwww.example.comになります。
        // define('URL_BASE', 'http://www.example.com');
        defined('URL_BASE') || define('URL_BASE', 'http://default.example.com');
        echo 'URL_BASE is ', URL_BASE;
    ?>
</body>
</html>