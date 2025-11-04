<?php
    # プログラム名：カフェメニュー名と合計金額計算プログラム
    # 概要：カフェメニューのメニュー名を配列化し、配列で管理し、さらに注文した数によって合計金額を算出するプログラム。
    class CafeMenu{
        # プロパティ
        public $name;
        public $price;
        public $count;

        # コンストラクタ
        public function __construct($name, $price, $count) {
            $this->name = $name;
            $this->price = $price;
            $this->count = $count;
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

        # 注文数によった合計金額を計算するメソッド
        public function result() {
            $result = $this->price * $this->count;
            return $result;
        }
    }

    # 実行部分
    $cafelatte = new CafeMenu('カフェラテ', '400', 2);
    $chocolatecake = new CafeMenu('チョコケーキ', '500', 1);
    $icetea = new CafeMenu('アイスティー', '350', 3);

    # 連想配列に入れる
    $menu = [
        [
            'name' => $cafelatte->name,
            'price' => $cafelatte->price,
            'count' => $cafelatte->count,
            'result' => $cafelatte->result()
        ],
        [
            'name' => $chocolatecake->name,
            'price' => $chocolatecake->price,
            'count' => $chocolatecake->count,
            'result' => $chocolatecake->result()
        ],
        [
            'name' => $icetea->name,
            'price' => $icetea->price,
            'count' => $icetea->count,
            'result' => $icetea->result()
        ]
    ];

    # 表示
    foreach ($menu as $menu_only => $value) {
        echo "{$value['name']}：{$value['price']}円 ✕ {$value['count']}個→小計：{$value['result']}円";
        echo '<br>';
    }
    echo '-------------------------';
    $all_result = $menu[0]['result'] + $menu[1]['result'] + $menu[2]['result'];
    echo '<br>';
    echo "合計金額：{$all_result}円";