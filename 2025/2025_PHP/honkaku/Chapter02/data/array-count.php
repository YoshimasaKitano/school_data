<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello World - honkaku</title>
</head>
<body>
    <?php
        // 配列の要素数を得る
        $chars = ['a', 'b', 'c'];
        echo count($chars), PHP_EOL;    // 結果：3

        // 連想配列の要素数を得る
        $chars = [
            'a' => 'あ',
            'i' => 'い',
            'u' => 'う',
            'e' => 'え',
            'o' => 'お'
        ];
        echo count($chars), PHP_EOL;    // 結果:5
    ?>
</body>
</html>