<?php declare(strict_types=1); ?>
<body>
<?php
    // データを出力する関数。
    // object型の宣言で、stdClassも受け取ることができる
    function printData(objec $data): void
    {
        print_r($data);
    }

    $data = new stdClass();
    $data->name = 'Tarou';
    $data->address = '東京都';
    $data->age = 28;
    printData($data);
?>
</body>