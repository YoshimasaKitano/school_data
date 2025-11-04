<?php declare(strict_types=1); ?>
<body>
<?php
    $hobbies = ['テニス', '散歩', 'バッティング練習'];
    $hobbiesAsString = implode('・', $hobbies);
    echo '趣味：', $hobbiesAsString, PHP_EOL;
?>
</body>