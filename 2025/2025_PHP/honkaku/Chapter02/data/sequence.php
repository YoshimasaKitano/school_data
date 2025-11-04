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
        $mailBody  = "お問い合わせを受け付けました。 \n\n";
        $mailBody .= "■お問い合わせ内容：\n";
        $mailBody .= "\t商品番号「abc123」についてサイズを教えてください。";
    ?>
    <p><pre><?=$mailBody?></ple></p>
</body>
</html>