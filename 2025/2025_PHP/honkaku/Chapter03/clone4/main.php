<?php declare(strict_types=1); ?>
<body>
<?php
    // タスク
    class Task
    {
        // タスク名
        public $name;
    }

    $task1 = new Task();
    $task1->name = 'パスポートの更新';
    $task2 = $task1;
    $task3 = clone $task1;

    var_dump($task1 == $task2); // 出力結果「true」
    var_dump($task1 === $task2); // 出力結果「true」

    var_dump($task1 == $task3); // 出力結果「true」
    var_dump($task1 === $task3); // 出力結果「false」
?>
</body>