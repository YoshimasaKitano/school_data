<?php
    # プログラム名：カフェメニュープログラム
    # 概要：カフェのメニュー名と料金を表示し、さらに割引率を指定して、新しい価格を表示することができるプログラム。
    class CafeMenu{
        # プロパティ
        public $name;
        public $price;

        # コンストラクタ
        public function __construct($name, $price) {
            $this->name = $name;
            $this->price = $price;
        }

        # メニュー名と料金を表示するメソッド
        public function show() {
            $message = $this->name .'：' .$this->price .'円';
            return $message;
        }

        # 割引率を指定して、新しい価格を表示するメソッド
        public function discount($rate) {
            $rate_now = 100 - (int)$rate;
            $rate_price = $this->price * ($rate_now / 100);
            $message = $rate .'％割引後の価格：' .$rate_price .'円';
            return $message;
        }
    }

    # カフェラテインスタンスの作成
    $cafelatte = new CafeMenu('カフェラテ', '400');
    echo $cafelatte->show();
    echo '<br>';

    # チョコケーキインスタンスの作成
    $chocolatecake = new CafeMenu('チョコケーキ', '500');
    echo $chocolatecake->show();
    echo '<br>';

    # 割引率10%のカフェラテの値段
    echo $cafelatte->discount(10);
    echo '<br>';

    # 割引率20%のチョコケーキの値段
    echo $chocolatecake->discount(20);
    echo '<br>';

