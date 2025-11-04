<?php

//オブジェクト思考・3---------------------

//「継承」extendsを使って継承もとのデータと同じデータ形式で作ること
//「オーバーライド」

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
    public function getData(){
        $message = '学生:' .$this->name .'-' .$this->gender .'-' .$this->age .'-' .$this->address;
        return $message;
    }  
}

//extendsでStudentListを継承
class TeacherList extends StudentList{
    //継承したTeacherListでメソッドを上書きすることをオーバーライドという
    public function getData(){
        $message = '担任:' .$this->name .'-' .$this->gender .'-' .$this->age .'-' .$this->address;
        return $message;
    }  
}

//担任リスト
$maruyama = new TeacherList('丸山先生', '男性', '50', '奈良県');
echo $maruyama->getData();
echo '<br>';

$katou = new TeacherList('加藤先生', '男性', '28', '大阪府');
echo $katou->getData();