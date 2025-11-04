<?php declare(strict_types=1); ?>
<body>
<?php
    require_once dirname(__FILE__) . '/Office/Word/Writer.php';
    class SomeClass
    {
        use Office\Word\Writer; // エラーになる
    }
?>
</body>