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
        $airports = ['Haneda', 'Narita', 'Chubu'];
        $airports[] = 'Kansai'; // 空港を追加
        $airports[] = 'Naha'; // 空港を追加

        // 以下のコメントアウトを外すとChubuがSendaiに上書きされます。
        //$airports[2] = 'Sendai'
    ?>
    <p><?=$airports[0]?></p>
    <p><?=$airports[1]?></p>
    <p><?=$airports[2]?></p>
    <p><?=$airports[3]?></p>
    <p><pre><?php print_r($airports);?></ple></p>
</body>
</html>