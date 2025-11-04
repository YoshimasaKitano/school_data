<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>演習問題解答</title>
</head>
<body>
    <?php
    // ①変数を使って自分の名前を表示しなさい。
    // 実行イメージ　　私の名前は○○です（全角フルネーム）
    $name = '山田太郎';

    // 連結出力
    echo '私の名前は' .$name .'です';
    echo '<br>';

    // 次々出力
    echo '私の名前は', $name, 'です';
    echo '<br>';

    // 変数展開出力
    echo "私の名前は{$name}です";
    echo '<br>';

    // ②変数3つを宣言し計算結果を表示しなさい。計算結果を格納する変数は0で初期化すること。（0で初期化=0で初期値を設定）
    // 実行イメージ　　加算結果：30

    $num1 = 10;
    $num2 = 10;
    $num3 = 10;
    $sum = 0;
    $sum = $num1 + $num2 + $num3;
    echo '加算結果：' .$sum;
    echo '<br>';

    // ③定数命令を使って、1,000円の商品を購入した時の税込価格（消費税率10%）を計算しなさい。
    // 実行イメージ　　税込み1100円

    define('TAX', 1.10);
    $total = 1000 * TAX;
    echo '税込み' .$total .'円';
    echo '<br>';

    // ④配列$fruitsを定義し値を代入しなさい。代入した結果を出力しなさい。
    // 実行イメージ　　Array ( [0] => apple [1] => orange [2] => lemon )

    $fruits = [];
    $fruits[0] = 'apple';
    $fruits[1] = 'orange';
    $fruits[2] = 'lemon';
    print_r($fruits);
    echo '<br>';

    // ⑤パスワードが一致している場合は「パスワードは一致している」、一致していない場合は「パスワードは一致していない」と表示しなさい。2つの値を使って厳密な比較をすること。

    $password1 = 12345;
    $password2 = 45678;
    if($password1 === $password2){
        echo 'パスワードは一致している';
    }else{
        echo 'パスワードは一致していない';
    }
    echo '<br>';

    // ⑥if命令を使ってテストの点数を評価しなさい。100点なら「上級」、80点以上なら「中級」、60点以上なら「初級」、それ以外は「追試」とする。

    $test = 100;
    if($test == 100){
        echo '上級';
    }elseif($test >= 80){
        echo '中級';
    }elseif($test >= 60){
        echo '初級';
    }else{
        echo '追試';
    }
    echo '<br>';

    // ⑦値が偶数の場合、奇数の場合、0以下の場合を判断し、その結果を表示しなさい。
    // 実行イメージ　　（値が10の場合）10：偶数　（値が15の場合）15：奇数　（値が0以下の場合）0：0より大きい値を設定してください

    $num = -10;
    if($num > 0){
        if($num % 2 == 0){
            echo $num .'：偶数';
        }else{
            echo $num .'：奇数';
        }
    }else{
        echo $num .'0より大きい値を設定してください';
    }
    echo '<br>';

    // ⑧配列$argsに文字列'10'と'20'を代入しなさい。また、配列の文字列を数値に型変換（型キャスト）させて、計算結果を表示しなさい。※1行目「$args = [];」の続き2行目から記述すること。
    // 実行イメージ　　10+20=30

    $args = [];
    $args[0] = '10';
    $args[1] = '20';
    $args1 = (int)$args[0];
    $args2 = (int)$args[1];
    $sum = $args1 + $args2;
    
    echo "{$args1} + {$args2} = {$sum}";
    echo '<br>';

    // ⑨while命令を使って文字列を5回繰り返して表示しなさい。
    /* 実行イメージ
    　 PHP復習：1回目
    　 PHP復習：2回目
    　 PHP復習：3回目
    　 PHP復習：4回目
    　 PHP復習：5回目
    */

    $i = 0;
    while($i < 5){
        $i++;
        echo "PHP復習：{$i}回目<br>";
    }

    // ⑩for命令とcount関数を使って、配列 [65, 40, 80, 33, 100] から最大値と最小値を取り出し表示しなさい。
    /* 実行イメージ
       最大値：100
       最小値：33
    */

    $data = [65, 40, 80, 33, 100];
    $max = $data[0];
    $min = $data[0];
    for($i = 1; $i < count($data); $i++){
        if($max < $data[$i]){
            $max = $data[$i];
        }
        if($min > $data[$i]){
            $min = $data[$i];
        }
    }
    echo '最大値：'. $max;
    echo '<br>';
    echo '最小値：'. $min;
    echo '<br>';

    // ⑪for命令とcontinue命令を使って、1～100までの奇数の合計を計算しなさい。
    // 実行イメージ　　奇数の合計値は〇〇です

    $total = 0;
    for($i = 0; $i <= 100; $i++){
        if($i % 2 == 0){
            continue;
        }
        $total += $i;
    }
    echo "奇数の合計値は{$total}です";
    echo '<br>';
    // ⑫foreach命令とリファレンス渡しを使って配列の値を一律に1.5倍に計算し表示しなさい。
    // 実行イメージ　　Array ( [0] => 15 [1] => 45 [2] => 90 )

    $data = [10, 30, 60];
    foreach($data as &$value){
        $value *= 1.5;
    }
    unset($value); // ループ処理が終わったあとはunset命令でリファレンスを消す
    print_r($data);
    echo '<br>';

    // ⑬if命令と論理演算子を使って変数$languageの値が「HTML」、「CSS」、「JavaScript」であれば「クライアントが理解する言語」と表示し、「PHP」、「Python」であれば「サーバーが理解する言語」と表示しなさい。

    $language = 'PHP';
    if($language == 'HTML' || $language == 'CSS' || $language == 'JavaScript'){
        echo 'クライアントが理解する言語';
    }
    if($language == 'PHP' || $language == 'Python'){
        echo 'サーバーが理解する言語';
    }
    echo '<br>';

    // ⑭連想配列$usersに値を代入しなさい。また、$keyと$valueを使って値を出力しなさい。
    /* 実行イメージ
       name - 山田
       age - 20
       address - 大阪
    */

    $users = [];
    $users['name'] = '山田';
    $users['age'] = 20;
    $users['address'] = '大阪';
    foreach($users as $key => $value){
        echo "{$key} - {$value}<br>";
    }

?>
</body>
</html>