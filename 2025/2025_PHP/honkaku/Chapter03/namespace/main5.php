<?php declare(strict_types=1); ?>
<body>
<?php
    require_once dirname(__FILE__) . '/Office/Word/Writer.php';
    use Office\Word\Writer;
    class SomeClass
    {
        public function __construct() {
            $writer = new Writer();
            $writer->write();
        }
    }
    $c = new SomeClass();
?>
</body>