<?php declare(strict_types=1); ?>
<body>
<?php
    $item = '万能MIXERーご自宅でかんたんにジュースやスムージー、なんとふりかけまで！ ';
    echo mb_strimwidth($item, 0, 20, '・・・'); // 結果：「万能MIXERーご自宅で・・・」
?>
</body>