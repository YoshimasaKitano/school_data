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
        $itemNumber = 'abc123';

        //ヒアドキュメント
        $mailBody = <<< MAIL
お問い合わせを受け付けました。

■お問い合わせ内容：
    商品番号「{$itemNumber}」について、"サイズ"と'色の種類'を教えてください。
MAIL;
    ?>
    <p><pre><?=$mailBody?></ple></p>
</body>
</html>