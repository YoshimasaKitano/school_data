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
        $name = 'おかもとあっつん';
        echo $name .'Hello World!';
    ?>

    <?php
        $sports = ['basketball', 'baseball'];
    ?>
    <p><pre><?php print_r($sports);?></pre></p>

    <?php
        $text = [
            ['あ', 'い', 'う', 'え', 'お'], 
            ['か', 'き', 'く', 'け', 'こ']
        ];
    ?>
    <p><?php echo $text[0][1], $text[1][0];?></p>

    <?php
        $user = [
            'name' => '北野善聖',
            'prefecture' => 'Osaka',
            'age' => 18,
            'hobby' => 'Video games',
        ];
    ?>
    <p><?=$user['name'];?></p>
</body>
</html>