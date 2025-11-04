<?php declare(strict_types=1); ?>
<body>
<?php
    echo '●変更前のコード：', mb_internal_encoding(), PHP_EOL;
    // 文字コードを変更する
    mb_internal_encoding('SJIS-Win');

    echo '●変更後の文字コード：', mb_internal_encoding(), PHP_EOL;
?>
</body>