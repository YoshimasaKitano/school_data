<?php declare(strict_types=1); ?>
<body>
<?php
    echo '●現在のUnixタイム：', PHP_EOL;
    echo time(), PHP_EOL;

    echo '●現在日時を出力：', PHP_EOL;
    echo date('Y-m-d H:i:s'), PHP_EOL;

    echo '現在の3日後の日時を出力(time使用)：', PHP_EOL;
    echo date('Y-m-d H:i:s', time() +60 * 60 * 24 * 3), PHP_EOL;

    echo '●現在の3日後の日時を出力(strtotime使用)：', PHP_EOL;
    echo date('Y-m-d H:i:s', strtotime('+3 days')), PHP_EOL;

    echo '●2019-01-10 10:00:00の3時間前を出力：', PHP_EOL;
    echo date('Y-m-d H:i:s', strtotime('-3 hours', strtotime('2019-01-10 10:00:00'))), PHP_EOL;

    $date1 = '2019-02-25 09:23:00';
    $date2 = '2019-02-25 17:12:34';

    echo '●$date1は$date2よりも未来か？：', PHP_EOL;
    var_dump(strtotime($date1) > strtotime($date2));

    echo '●$date1は$date2よりも過去か？：', PHP_EOL;
    var_dump(strtotime($date1) < strtotime($date2));
?>
</body>