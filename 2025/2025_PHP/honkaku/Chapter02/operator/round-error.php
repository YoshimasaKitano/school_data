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
        /* (0.1 + 0.7) × 10 を切り捨てします */

        // 実際に計算する例(丸め誤差が起きる)
        $result1 = floor(0.1 + 0.7) * 10;

        // 文字列型にキャストする(正しい計算状態になる)
        $result2 = floor((string)(0.1 + 0.7) * 10);

        // BCMath関数を使って計算する(正しい計算状態になる)
        $result3 = floor((int)bcmul(bcadd(0.1, 0.7, 2), 10, 2));
    ?>
    <h4>(0.1 + 0.7) × 10の切り捨ての計算結果</h4>
    <p>result1：<?=$result1?></p>
    <p>result2：<?=$result2?></p>
    <p>result3：<?=$result3?></p>
</body>
</html>