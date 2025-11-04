<?php declare(strict_types=1); ?>
<body>
<?php
    require_once dirname(__FILE__) . '/Task.php';
    $task = new Task();
    $task->priority = Task::PRIORITY_HIGH;
    echo '優先度：', $task->getPriorityAsString();
?>
</body>