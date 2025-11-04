<?php declare(strict_types=1); ?>
<body>
<?php
    $today = '2019-03-16';

    // ハイフンで分割した結果を、そのまま配列で受け取る例
    $dataElements = explode('-', $today);
    print_r($dataElements); // 結果：Array([0] => 2019 [1] => 03 [2] => 16)

    // ハイフンで分割した結果を、list()でスカラー変数に分けて受け取る例
    list($year, $month, $day) = explode('-', $today);
    echo '年：', $year, PHP_EOL;    // 結果：2019
    echo '月：', $month, PHP_EOL;    // 結果：03
    echo '日：', $day, PHP_EOL;    // 結果：16
?>
</body>