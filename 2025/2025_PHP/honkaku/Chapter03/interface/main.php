<?php declare(strict_types=1); ?>
<body>
<?php
    require_once dirname(__FILE__) . 'Bird.php';
    $bird = new Bird();
    $bird->fly();
    $bird->walk();
?>
</body>