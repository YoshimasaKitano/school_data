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
        $point = 55;
        $message = '通常スコアです。';
        if ($point >= 80) {
            $message = 'ハイスコアです。';
        } elseif ($point >= 50) {
            $message = 'ミドルスコアです。';
        }
    ?>
    <p>メッセージ：<?=$message?></p>
</body>
</html>