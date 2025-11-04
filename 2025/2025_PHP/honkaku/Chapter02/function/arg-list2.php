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
        //　複数の数値を足し算して返す関数。
        function add(string $header, int $number1, int $number2, int $number3 = 0): string
        {
            $total = $number1 + $number2 + $number3;
            return $header .$total;
        }

        // add関数に渡す数値配列。
        $numbers =[3, 2, 4];

        //　以下の場合、引数$number2が足りないため、エラーとなります。
        // $numbers = [3];

        // 以下の場合、引数$number3にはデフォルト値の0がセットされます。
        // $numbers = [3, 2];

        // 以下の場合、4番目の要素「12」は無視され、計算結果は「9」となります。
        // $numbers = [3, 2, 4, 12];

        $result = add('計算結果：', ...$numbers);
        echo $result;
    ?>
</body>
</html>