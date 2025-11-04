<?php declare(strict_types=1); ?>
<body>
<?php
    abstract class Clock
    {
        // 時間をセットする
        public function setTime(int $time): void
        {
            echo 'ClockクラスのsetTimeメソッドが呼ばれました。', PHP_EOL;
        }
    }

    class DigitalClock extends Clock
    {
        // 時間をセットする(オーバーライド)
        public function setTime(int $time): void
        {
            echo 'DigitalClockクラスのsetTimeメソッドが呼ばれました。', PHP_EOL;
            parent::setTime($time);
        }
    }

    // メインルーチン
    $currentTime = strtotime('2018-08-22 17:15');
    $digitalClock = new DigitalClock();
    $digitalClock->setTime($currentTime);
?>
</body>