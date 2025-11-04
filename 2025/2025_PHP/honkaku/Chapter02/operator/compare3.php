<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
<?php $point = 85; ?>
<?php
    var_dump($point <=> 85); // 結果0
    var_dump($point <=> 70); // 結果1
    var_dump($point <=> 99); // 結果-1
?>
</body>
</html>