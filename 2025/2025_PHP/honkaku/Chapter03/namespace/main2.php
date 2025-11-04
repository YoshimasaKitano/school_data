<?php declare(strict_types=1); ?>
<body>
<?php
    require_once dirname(__FILE__) . '/Office/File.php';
    $file = new Office\File();
    $file->setWordProperty();
    $file->setExcelProperty();
?>
</body>