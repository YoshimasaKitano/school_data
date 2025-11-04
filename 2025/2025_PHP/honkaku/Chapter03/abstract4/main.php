<?php declare(strict_types=1); ?>
<body>
<?php
    abstract class Clock
    {
        public function setTime(string $time, $extraArguments = null)
        {
            // 何らかの処理
        }
    }
    class DigitalClock extends Clock
    {
        public function setTime(string $time, $extraArguments = null)
        {
            // デジタル時計特有の何らかの処理
            // $extraArguments引数を使って、文字色(fontColor)のデータも受け取る。
        }
    }
    class AnalogClock extends Clock
    {
        public function setTime(string $time, $extraArguments = null)
        {
            // アナログ時計特有の何らかの処理
            // $extraArguments引数は無視する。
        }
    }

    // メインルーチン
    $digitalClock = new DigitalClock();
    $digitalClock->setTime('11:14', ['fontcolor' => 'white']);
    $analogClock = new AnalogClock();
    $analogClock->setTime('11:14');
?>
</body>