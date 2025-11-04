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
        $colors = [
            'red' => '赤',
            'blue' => '青',
            'yellow' => '黄'
        ];
        foreach ($colors as $key => $value) {
            echo "<p>キー：($key) 値：($value)</p>";
        }
    ?>
</body>
</html>