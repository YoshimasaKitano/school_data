<?php declare(strict_types=1); ?>
<body>
<?php
    $number = 987.654;

    echo round($number), PHP_EOL;       // 結果：988
    echo round($number, 1), PHP_EOL;       // 結果：987.7
    echo round($number, 2), PHP_EOL;       // 結果：987.65
    echo round($number, 3), PHP_EOL;       // 結果：987.654
    echo round($number, 4), PHP_EOL;       // 結果：987.654
    echo round($number, -1), PHP_EOL;       // 結果：990
    echo round($number, -2), PHP_EOL;       // 結果：1000

    echo ceil($number), PHP_EOL;        // 結果：988

    echo floor($number), PHP_EOL;       // 結果：987
?>
</body>