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
        $addFunction = function ($a, $b) {
            return $a + $b;
        };
        $total = $addFunction(10, 20);
    ?>
    <p>計算結果：<?=$total?></p>
</body>
</html>