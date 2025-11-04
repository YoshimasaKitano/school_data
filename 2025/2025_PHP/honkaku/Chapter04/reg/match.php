<?php declare(strict_types=1); ?>
<body>
<?php
    $mathed = [];

    echo '●住所から郵便番号を見つける', PHP_EOL;
    $address = '123-4567 東京都豊島区...';
    preg_match('/\A[0-9]{3}\-[0-9]{4}/u', $address, $mathed, PREG_OFFSET_CAPTURE); // 123-4567がマッチする
    print_r($mathed);

    echo '●文字列から16進数表記のカラーコードを見つける', PHP_EOL;
    $string = 'darkviolet - 濃いすみれ色 - #9400d3a';
    preg_match('/#[0-9a-f]{6}/ui', $string, $mathed, PREG_OFFSET_CAPTURE); // #9400d3がマッチする
    prit_r($mathed);

    echo '●半角数字およびハイフンのみかを入力チェックする', PHP_EOL;
    $input = '03- ９９９９-0000';
    if (preg_match('/\A[0-9\-]+\z/u', $input)) {
        echo '入力に問題がありません。', PHP_EOL;
    } else {
        echo '半角数字とハイフンのみで入力してください。', PHP_EOL; // こちらが出力される
    }

    echo '●半角英数字のみかを入力チェックする', PHP_EOL;
    $input = 'Hello123';
    if (preg_match('/\A[a-zA-Z0-9]+\z/u', $input)) {
        echo '入力に問題ありません。', PHP_EOL; // こちらが出力される
    } else {
        echo '半角英数字のみで入力してください。', PHP_EOL;
    }

    echo '●半角英数字のみかを入力チェックする(i修飾子)', PHP_EOL;
    $input = 'Hello123';
    if (preg_match('/\A[a-z0-9]+\z/ui', $input)) {
        echo '入力に問題ありません。', PHP_EOL; // こちらが出力される
    } else {
        echo '半角英数字のみで入力してください。', PHP_EOL;
    }
?>
</body>