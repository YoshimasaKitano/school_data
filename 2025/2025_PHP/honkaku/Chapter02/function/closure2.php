<?php declare(strict_types=1); ?>
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
        $greeting = 'Good';

        // クロージャーの定義。useを使って$greetingを引き継ぎます。
        $greetingMaker = function ($time) use ($greeting) {
            print $greeting .' ' .$time .'<br>';
        };

        // 出力結果は「Good Morning」
        $greetingMaker('Morning');

        // 一見「Beautiful Evening」が出力されそうなものですが「Good Evening」が出力されます。
        // useで引き継がれるのは関数が定義された時点での$greetingの値だからです。
        // クローシャーの定義時に「use (&$greeting)」とリファレンス私で引き継ぐことで、
        // 「Beautiful」が出力されるようになります。
        $greeting = 'Beautiful';
        $greetingMaker('Evening');
    ?>
</body>
</html>