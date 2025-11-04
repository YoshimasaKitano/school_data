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
        $bool1 = false;
        $bool2 = true;
        $bool3 = true;
        if ($bool1 === true) {
            echo '$bool1は真です。';
        } elseif ($bool2 === true) {
            echo '$bool2は真です。';
        }elseif ($bool3 === true) {
            echo '$bool3は真です。';
        }
    ?>
    <?php
        $bool1 = false;
        $bool2 = true;
        $bool3 = true;
        if ($bool1 === true) {
            echo '$bool1は真です。';
        } 
        if ($bool2 === true) {
            echo '$bool2は真です。';
        }
        if ($bool3 === true) {
            echo '$bool3は真です。';
        }
    ?>
</body>
</html>