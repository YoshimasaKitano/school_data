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
        $value = 'World';

        // 文字列演算子(.)による値と変数の連結
        $combined1 = 'Hello' . $value . ' ! ';

        // 変数の展開。ダブルクオート内で使用可能
        $combined2 = "Hello{$value} ! ";

        // 代入演算子(=)と文字列演算子(.)の組み合わせ
        $combined3 = 'Hello';
        $combined3 .= $value;
        $combined3 .= ' ! ';

        // シングルオートないでは変数は展開されない
        $combined4 = 'Hello {$value} ! ';
    ?>
    <p><?=$combined1?></p>
    <p><?=$combined2?></p>
    <p><?=$combined3?></p>
    <p><?=$combined4?></p>
</body>
</html>