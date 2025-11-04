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
        function add()
        {
            // globalキーワードを使い、関数外で定義された$num1, $num2を関数内で使えるようにする
            global $num1, $num2;
            return $num1 + $num2;
        }
        // メインルーチン
        $result = add();
        echo $result;
    ?>
</body>
</html>