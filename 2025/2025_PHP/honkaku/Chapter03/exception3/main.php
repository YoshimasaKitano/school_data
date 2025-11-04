<?php declare(strict_types=1); ?>
<body>
<?php
    require_once dirname(__FILE__) . '/ClassA.php';
    try {
        $classA = new ClassA();
        $classA->methodA();
    } catch (Exception $exception) {
        echo 'メインルーチンで例外をキャッチ。エラー内容：', $exception->getMessage(), PHP_EOL;
    }
    echo 'Main routine completed.';
?>
</body>