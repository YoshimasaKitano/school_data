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
            echo 'スコアは正の数でなければなりません。';
            exit(1); // 終了コードを返して終了
        }
        echo 'スコアは：', $score, '点です。'; // この命令は実行されない
    ?>
</body>
</html>