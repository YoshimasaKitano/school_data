<?php
    # プログラム名：お客さんによってのカフェメニュー名と合計金額計算プログラム
    # 概要：お客さんごとに注文されたカフェメニューのメニュー名を配列化し、配列で管理し、さらに注文した数によって合計金額を算出するプログラム。
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

    class CafeCustomer{
        # プロパティ
        public $customer;
        public $orders = [];

        # コンストラクタ
        public function __construct($customer) {
            $this->customer = $customer;
        }

        # 注文を追加するメソッド
        public function addorder(CafeMenu $order_menu) {
            $this->orders[] = $order_menu;
        }

        # 注文内容を表示するメソッド
        public function showOrders() {
            $total = 0;
            $order_list = [];
            array_push($order_list, "【お客様】{$this->customer}さん");
            array_push($order_list, "【ご注文内容】");
            foreach ($this->orders as $order) {
                $total = $order->result();
                array_push($order_list, " - {$order->name}：{$order->price}円 × {$order->count}個 → 小計：{$total}円");
            }
            return $order_list;
        }
    }

    # 実行部分
    $cafelatte = new CafeMenu('カフェラテ', '400', 2);
    $chocolatecake = new CafeMenu('チョコケーキ', '500', 1);
    $icetea = new CafeMenu('アイスティー', '350', 3);

    $order_customer = new CafeCustomer('佐藤');

    $order_customer->addorder($cafelatte);
    $order_customer->addorder($chocolatecake);
    $order_customer->addorder($icetea);
    $all_price = $cafelatte->result() + $chocolatecake->result() + $icetea->result();

    # 注文内容を表示
    $order_list_totals = $order_customer->showOrders();
    foreach ($order_list_totals as $order_list_total) {
        echo $order_list_total;
        echo '<br>';
    }
    echo '-------------------------';
    echo '<br>';
    echo "合計金額：{$all_price}円";
    
