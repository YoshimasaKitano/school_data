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
        $chars = [
            ['あ', 'い', 'う', 'え', 'お'],
            ['か', 'き', 'く', 'け', 'こ'],
            ['さ', 'し', 'す', 'せ', 'そ']
        ];
        $chars[] = ['た', 'ち', 'つ', 'て', 'と'];
    ?>
    <p>chars[0][0]：<?=$chars[0][0]?></p>
    <p>chars[0][1]：<?=$chars[0][1]?></p>
    <p>chars[0][2]：<?=$chars[0][2]?></p>
    <p>chars[1][0]：<?=$chars[1][0]?></p>
    <p>chars[1][1]：<?=$chars[1][1]?></p>
    <p>chars[1][2]：<?=$chars[1][2]?></p>
    <p><pre><?php print_r($chars);?></ple></p>
</body>
</html>