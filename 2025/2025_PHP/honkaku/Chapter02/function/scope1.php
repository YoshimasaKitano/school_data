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
        $num1 = 3;
        $num2 = 10;

        /* 2つの数値を足し算して出力する関数 */
        function add($a, $b)
        {
            echo '$num1を出力します：', $num1;
        }

        // メインルーチン
        $result = add($num1, $num2);
        echo '$aを出力します：', $a;
    ?>
</body>
</html>