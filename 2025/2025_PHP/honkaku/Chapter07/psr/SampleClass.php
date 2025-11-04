<?php

// ・class、extends、implementsキーワードは同じ行に書く(MUST)
// ・クラスの開始の波括弧は独立した行に書く(MUST)
// ・クラスの開始の波括弧の前後に空行があってはならない(MUST NOT)
class SampleClass extends ParentClass implements SomeInterface
{
    // ・プロパティのアクセス修飾子は必ず付ける(MUST)
    // ・1行で2つ以上のプロパティを定義してはならない(MUST NOT)
    public $publicProperty = null;

    // ・publicでないことを示すために1文字目にアンダースコアを使わない(MUST NOT)
    // つまり$_privatePropertyではなく$privatePropertyとする
    private $privateProperty = null;

    // ・staticを付けるときはアクセス修飾子の後に書く(MUST)
    protected static $staticProperty;

    // ・メソッドのアクセス修飾子は必ず付ける(MUST)
    // ・メソッド名の直後にスペースは入れない(MUST NOT)
    // ・引数を表す丸括弧が開いた直後、閉じる直前にスペースを入れない(MUST NOT)
    // ・引数を列挙するときのカンマの前にスペースを入れない(MUST NOT)
    // ・引数を列挙するときのカンマの後にスペース1つを入れる(MUST)
    public function doSomething1(string $arg1, int $arg2)
    { // ←開始の波括弧は行を分ける(MUST)
        
        // 処理...

    } // ←終了の波括弧も行を分ける(MUST)

    // ・引数のnullを許可するクエスチョン記号とデータ型の間にスペースを入れない(MUST NOT)
    // ・引数の参照渡しを表すアンパサンド記号と引数名の間にスペースを入れない(MUST NOT)
    // ・デフォルト値をもつ引数は最後に書く(MUST)
}