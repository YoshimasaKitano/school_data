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
        $score = -100;
        if ($score < 0) {
            die('スコアは正の数でなければいけません。'); // 出力して終了
        }
        echo 'スコアは：', $score, '点です。'; // この命令は実行されない
    ?>
</body>
</html>