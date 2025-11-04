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
        // 複数の数値を足し算して返す関数。
        // 可変長引数は最後の引数にしか使えないことに注意してください。
        function add(string $header, int ...$numbers): string
        {
            $total = 0;
            foreach ($numbers as $number) {
                $total += $number;
            }
            return $header .$total;
        }

        $result = add('計算結果：', 3, 2, 9, 1);
        echo $result;
    ?>
</body>
</html>