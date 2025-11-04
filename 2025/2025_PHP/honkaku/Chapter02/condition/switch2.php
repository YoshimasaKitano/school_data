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
        $number = 1;
        switch ($number) {
            case 0 :
            echo 'number=0の処理<br>';
            case 1 :
                echo 'number=1の処理<br>';
            case 2 :
                echo 'number=2の処理<br>';
            default :
                echo 'defaultの処理<br>';
        }
    ?>
</body>
</html>