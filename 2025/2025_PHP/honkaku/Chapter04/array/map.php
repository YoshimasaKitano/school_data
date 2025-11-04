<?php declare(strict_types=1); ?>
<body>
<?php
    // 有効期限リスト
    $expireDates = ['2020-01-03', '2021-12-11', '2019-08-10'];

    $newExpireDates = array_map(
        // 有効期限を3年間延長する関数(引数$callback)
        function($date) {
            return (new DateTime($date))->date_modify('+ 3years')->format('Y-m-d');
        },
        $expireDates
    );

    echo '●expireDatesの要素(内容はもとのまま)', PHP_EOL;
    print_r($expireDates);

    echo '●newExpireDatesの要素(内容が書き換わっています)', PHP_EOL;
    print_r($newExpireDates);
?>
</body>