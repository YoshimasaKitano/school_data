<?php declare(strict_types=1); ?>
<body>
<?php
    require_once dirname(__FILE__) . '/Office/Word/Writer.php';
    require_once dirname(__FILE__) . '/Office/Excel/Writer.php';

    $writer = new \Office\Word\Writer();
    $writer->write();

    $writer = new \Office\Excel\Writer();
    $writer->write();
?>
</body>