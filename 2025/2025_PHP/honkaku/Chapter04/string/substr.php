<?php declare(strict_types=1); ?>
<body>
<?php
    $sentence = '今日は、良い日です';
    var_dump(mb_substr($sentence, 4, 3));      // 結果：良い日
    var_dump(mb_substr($sentence, -5, 3));      // 結果：良い日
    var_dump(mb_substr($sentence, 4));      // 結果：良い日です

    var_dump(mb_substr($sentence, '良', false));      // 結果：良い日です
    var_dump(mb_substr($sentence, '日', false));      // 結果：日は、良い日です
    var_dump(mb_substr($sentence, '日', true));      // 結果：今
?>
</body>