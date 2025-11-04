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
        $message = '';
        $extension = 'gif';
        switch ($extension) {
            case 'jpg' :
                $message = 'jpg画像です。';
                break;
            case 'png' :
                $message = 'png画像です。';
                break;
            case 'gif' :
                $message = 'gif画像です。';
                break;
            case 'bmp' :
            case 'svg' :
                $message = 'bmpまたはsvg画像です。';
                break;
            default :
                $message = 'その他の形式です。';
        }
    ?>
    <p>メッセージ：<?=$message?></p>
</body>
</html>