<?php declare(strict_types=1); ?>
<body>
<?php
    $sentence = '今日は、良い日です';
    var_dump(mb_stripos($sentence, '日'));      // 結果：1
    var_dump(mb_stripos($sentence, '無'));      // 結果：false
    var_dump(mb_stripos($sentence, '良い日'));      // 結果：4
    var_dump(mb_stripos($sentence, '日'));      // 結果：6

    if (mb_strpos($sentence, '日') !== false) {
        echo '引数$sentenceの中に「日」が見つかりました。', PHP_EOL;    // こちらのブロックに入ります。
    } else {
        echo '引数$sentenceの中に「日」は見つかりませんでした。', PHP_EOL;
    }
?>
</body>
