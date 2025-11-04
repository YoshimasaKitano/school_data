<?php //閉じタグを作るとから行や空白がバグになる

//オブジェクト思考・1---------------------------------

//「クラス」一つの処理（処理を役割分担する）
//「プロパティ」持っているデータ（状態を持たせる）

//「アクセス修飾子」メンバ変数やメソッドにどこからアクセスできるかの指定
//public    クラス内、クラス外のどこからでもアクセス可能
//private   同じクラス内からのみアクセス可能
//protected 同じクラス、および、クラスからアクセス可能

//「メンバ変数」オブジェクトの状態を表すデータを格納する変数
//「メソッド」データの操作をまとめたもので、オブジェクトの持つ機能

//クラス名StudentListを定義（設計）
//クラス名の一番初めは大文字
class StudentList{
    //プロパティを定義（状態の変数を定義すること）
    public $name;//publicはアクセス修飾子、$nameはメンバ変数（クラス内変数）
    public $gender;
    public $age;
    public $address;
}

//クラスから実体を生成することを「インスタンス化」
$suzuki = new StudentList(); //newで作成したもののことを「インスタンス」（suzukiがインスタンス、それをするのがインスタンス化）
$suzuki->name = '鈴木一郎'; //nameに$が必要ないのは「$suzukiのname」という変数だからと考えるのがGood
$suzuki->gender = '男子'; //アロー演算子 -> を使ってメンバ変数に値を入れる
$suzuki->age = '18';
$suzuki->address = '大阪市';

//「鈴木一郎」を出力するには？
echo '学生:', $suzuki->name;
echo '<br>';

$abe = new StudentList();
$abe->name = '阿部花子';
$abe->gender = '女子';
$abe->age = '19';
$abe->address = '神戸市';

//「阿部花子」を出力するには？
echo '学生:', $abe->name;


