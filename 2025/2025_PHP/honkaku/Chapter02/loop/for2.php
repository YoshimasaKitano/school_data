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
    $lines = [
        'いろはにほへと',
        'ちりぬるを',
        'わかよたれそ',
    ];
    for ($lineNumber = 1; $lineNumber <= count($lines); $lineNumber++) {
        echo $lineNumber, '行目：', $lines[$lineNumber - 1], PHP_EOL;
    }
?>
</pre>
</body>
</html>