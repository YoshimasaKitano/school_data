<?php declare(strict_types=1); ?>
<body>
<?php
    require_once dirname(__FILE__) . '/Office/Word/Writer.php';
    require_once dirname(__FILE__) . '/Office/Excel/Writer.php';

    use Office\Word\Writer;
    $writer = new Writer(); // WordのWriteクラスを使う
    $writer->write();

    use Office\Excel\Writer; // ここでエラー！
    $writer = new Writer(); // ExcelのWriterクラスを使う
    $writer->write();
?>
</body>