<?php declare(strict_types=1); ?>
<body>
<?php
    require_once dirname(__FILE__) . '/Canvas.php';
    require_once dirname(__FILE__) . '/DigitalClock.php';
    require_once dirname(__FILE__) . '/AnalogClock.php';
    $canvas = new Canvas();

    $currentTime = strtotime('2018-08-22 17:15');
    $digitalClock = new DigitalClock();
    $digitalClock->setTime($currentTime);
    $canvas->drawClock($digitalClock); // 結果：17:15

    $analogClock = new AnalogClock();
    $analogClock->setTime($currentTime);
    $canvas->drawClock($analogClock); // 結果：長針：90° 短針：157.5°
?>
</body>