<?php declare(strict_types=1); ?>
<body>
<?php
    require_once dirname(__FILE__) . '/ExcelColumnConverter.php';
    echo ExcelColumnConverter::calcAlphabetColumnName(3), PHP_EOL; // 出力結果「D」
    echo ExcelColumnConverter::calcNumberColumnName('F'); // 出力結果「5」
?>
</body>