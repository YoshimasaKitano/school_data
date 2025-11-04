<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
<pre>
<?php
    $total = 0;
    $numbers = [10, 2, -5, 3, 'abc', 6, 1];
    echo '正の整数を対象に配列の要素を足し算します...', PHP_EOL;
    foreach ($numbers as $number) {
        if (!is_numeric($number)) {
            echo "数値ではない値を検出したため計算を中断します...(対象値：($number))", PHP_EOL;
            break;
        }
        if ($number < 0) {
            echo "マイナス値は計算しません...(対象地：($number))", PHP_EOL;
            continue;
        }
        $total += $number;
    }
    echo "■合計：($total)", PHP_EOL;
?>
</pre>
</body>
</html>