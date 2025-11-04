<?php declare(strict_types=1); ?>
<body>
<?php
    abstract class Clock
    {
        private $time;

        // コンストラクタ
        public function __construct(int $time)
        {
            echo 'Clockクラスのコンストラクタが呼ばれました。', PHP_EOL;
            $this->time = $time;
        }
    }

    class DigitalClock extends Clock
    {
        private $color;

        // コンストラクタ
        public function __construct(int $time, string $color)
        {
            echo 'DigitalClockクラスのコンストラクタが呼ばれました。', PHP_EOL;
            $this->color = $color;
            parent::__construct($time);
        }
    }

    // メインルーチン
    $currentTime = strtotime('2018-08-22 17:15');
    $digitalClock = new DigitalClock($currentTime, 'yellow');
?>
</body>