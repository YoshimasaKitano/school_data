<?php

//オブジェクト思考・２---------------------

//「メソッド」データの操作をまとめたもので、オブジェクトの持つ機能、関数
//「コンストラクタ」インスタンスが生成されたときに一番最初に呼び出される関数
// $thisはその時インスタンス化した時の変数の中身が代入される

//クラス名StudentListを定義（設計）
class StudentList{
    //プロパティを定義
    public $name;//publicはアクセス修飾子、$nameはメンバ変数（クラス内変数）
    public $gender;
    public $age;
    public $address;

    //コンストラクタの定義　（メソッドよりも先に動く）
    public function __construct($name, $gender, $age, $address){
        $this->name = $name;
        $this->gender = $gender;
        $this->age = $age;
        $this->address = $address;
    }

    //メソッドの定義
    public function getDate(){
        $message = '学生:' .$this->name .'-' .$this->gender .'-' .$this->age .'-' .$this->address;
        return $message;
    }  
}

$suzuki = new StudentList('鈴木一郎', '男子', '18', '大阪市');
echo $suzuki->getDate();

echo '<br>';

$abe = new StudentList('阿部花子', '女子', '19', '神戸市');
echo $abe->getDate();