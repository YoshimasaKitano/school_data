<?php
    # プログラム名：カフェメニュー名配列プログラム
    # 概要：カフェメニューのメニュー名を配列化し、配列で管理することができるプログラム
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

    # 実行部分
    $cafelatte = new CafeMenu('カフェラテ', '400');
    $chocolatecake = new CafeMenu('チョコケーキ', '500');
    $icetea = new CafeMenu('アイスティー', '350');

    # 連想配列に入れる
    $menu = [
        [
            'name' => $cafelatte->name,
            'price' => $cafelatte->price
        ],
        [
            'name' => $chocolatecake->name,
            'price' => $chocolatecake->price
        ],
        [
            'name' => $icetea->name,
            'price' => $icetea->price
        ]
    ];
    # 表示
    foreach ($menu as $menu_only => $value) {
        echo "{$value['name']}：{$value['price']}円"; 
        echo '<br>';
    }