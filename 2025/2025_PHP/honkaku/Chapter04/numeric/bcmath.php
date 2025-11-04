<?php declare(strict_types=1); ?>
<body>
<?php

    // 加算する
    echo bcadd('0.123', '0.234', 3), PHP_EOL;   // 結果：0.357
    echo bcadd('0.123', '0.234', 5), PHP_EOL;   // 結果；0.35700

    // べき乗する
    echo bcpow('1.2', '3', 3), PHP_EOL;         // 結果：1.728

    // 平方根を求める
    echo bcsqrt('2', 10), PHP_EOL;              // 結果：1.4142135623

    // 2つの値を比較する
    echo bccomp('0.12345', '0.123456', 3), PHP_EOL;     // 結果：0(等しい)
    echo bccomp('0.12345', '0.12346', 4), PHP_EOL;     // 結果：0(等しい)
    echo bccomp('0.12345', '0.12346', 5), PHP_EOL;     // 結果：-1(左オペランドのほうが小さい)
?>
</body>