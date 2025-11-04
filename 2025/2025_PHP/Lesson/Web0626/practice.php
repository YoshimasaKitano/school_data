<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>practice</title>
</head>
<body>
    <?php
    // <!-- 【演習問題・1】 -->

    // <!-- ①変数を使って自分の名前を表示しなさい。
    // 実行イメージ　　私の名前は○○です（全角フルネーム） -->
        $name = '北野善聖';
    // <!-- 連結出力 -->
    echo '私の名前は' .$name .'です<br>';
    // <!-- 次々出力 -->
    echo '私の名前は', $name, 'です<br>';
    // <!-- 変数展開出力 -->
    echo "私の名前は{$name}です<br>";
    // <!-- ②変数3つを宣言し計算結果を表示しなさい。計算結果を格納する変数は0で初期化すること。（0で初期化=0で初期値を設定）
    // 実行イメージ　　加算結果：30 -->
    $apple = 5;
    $grape = 7;
    $result = 0;
    $result = $apple + $grape;
    echo "加算結果：{$result}<br>";
    ?>
    <!-- ③定数命令を使って、1,000円の商品を購入した時の税込価格（消費税率10%）を計算しなさい。
    // 実行イメージ　　税込み1100円 -->
    <?php
        define('TAX_PERCENT', 0.1)
    ?>
    <p>税込み<?=1000 + 1000 * TAX_PERCENT;?>円</p>
    <?php echo '<br>'?>
    <!-- ④配列$fruitsを定義し値を代入しなさい。代入した結果を出力しなさい。
    // 実行イメージ　　Array ( [0] => apple [1] => orange [2] => remon ) -->
    <?php
        $fruits = ['apple', 'orange', 'remon'];
    ?>
    <p><pre><?php print_r($fruits);?></pre></p>
</body>
</html>