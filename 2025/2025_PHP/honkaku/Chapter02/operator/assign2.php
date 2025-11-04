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
        // $greeting2には値ではなく参照が入ります。
        $greeting1 = 'Hello';
        $greeting2 = &$greeting1;
        $greeting1 = 'World';
    ?>
    <p>greeting1：<?=$greeting1?></p>
    <p>greeting2：<?=$greeting2?></p>
</body>
</html>