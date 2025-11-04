<?php declare(strict_types=1); ?>
<body>
<?php
    require_once dirname(__FILE__) . '/DigitalClock.php';
    $currentTime = strtotime('2018-08-22 17:15');
    $digitalClock = new DigitalClock();
    $digitalClock->setTime($currentTime); // オーバーライドされたsetTime()が呼び出される
    echo $digitalClock->getColor();
?>
</body>