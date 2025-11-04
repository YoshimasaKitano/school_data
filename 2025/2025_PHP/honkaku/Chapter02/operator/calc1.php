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
        $num1 = 7 + 3;
        $num2 = 7 - 3;
        $num3 = 7 * 3;
        $num4 = 7 / 3;
        $num5 = 7 % 3;
        $num6 = 7 ** 3; // 7の3乗
    ?>
    <p>加算：<?=$num1?></p>
    <p>減算：<?=$num2?></p>
    <p>乗算：<?=$num3?></p>
    <p>除算：<?=$num4?></p>
    <p>あまり：<?=$num5?></p>
    <p>累乗：<?=$num6?></p>
</body>
</html>