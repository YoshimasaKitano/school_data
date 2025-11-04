<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
<pre>
<?php
    $num = 100;
    while ($num < 200) {
        echo $num, PHP_EOL;
        $num  += 30;
    }
    echo '$numが200を超えたためループを抜けました。';
?>
</pre>
</body>
</html>