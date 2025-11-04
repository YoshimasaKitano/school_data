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
        $sum = 3;
        $sum *= 5; // $sum = $sum * 5; と同じ意味

        $greeting = 'Hello ';
        $greeting .= 'World'; // $greeting = $greeting .'World'; と同じ意味
    ?>
    <p>sum：<?=$sum?></p>
    <p>$greeting：<?=$greeting?></p>
</body>
</html>