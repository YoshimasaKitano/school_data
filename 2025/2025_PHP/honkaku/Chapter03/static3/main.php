<?php declare(strict_types=1); ?>
<body>
<?php
    // 何らかのクラス
    class SomeClass
    {
        // インスタンスプロパティ
        private $instanceProperty;

        // 静的メソッド
        public static function staticMethod()
        {
            // インスタンスプロパティにアクセスする・
            // エラー「Using $this when not in object context」となる。
            $this->instanceProperty = 1;
        }
    }

    // メインルーチン
    SomeClass::staticMethod();
?>
</body>