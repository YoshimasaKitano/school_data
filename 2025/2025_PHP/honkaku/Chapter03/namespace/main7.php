<?php declare(strict_types=1); ?>
<body>
<?php
    require_once dirname(__FILE__) . '/Office/Word/Writer.php';
    require_once dirname(__FILE__) . '/Office/Excel/Writer.php';
    use Office\Word\Writer as WordWriter;
    use Office\Excel\Writer as ExcelWriter;

    $writer = new WordWriter(); // WordのWriterクラスを使う
    $writer->write();

    $writer = new ExcelWriter(); // ExcelのWriteクラスを使う
    #writer->$write()
?>
</body>