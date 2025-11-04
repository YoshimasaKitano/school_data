<?php declare(strict_types=1); ?>
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
        /* 税込金額を計算する関数 */
        function calcPriceWithTax(int $price, float $tax = 0.10): float
        {
            $result = $price * (1 + $tax);
            return $result;
        }

        // メインルーチン
        $priceWithTax = calcPriceWithTax(1000);
        echo "<p>計算結果：{$priceWithTax}</p>";

        $priceWithTax = calcPriceWithTax(1000, 0.05);
        echo "<p>計算結果：{$priceWithTax}</p>";
    ?>
</body>
</html>