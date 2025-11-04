<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
<!-- 【演習問題・2】 -->

<!-- ⑤パスワードが一致している場合は「パスワードは一致している」、一致していない場合は「パスワードは一致していない」と表示しなさい。2つの値を使って厳密な比較をすること。 -->
    <?php
        $key = 1111;
        $key_key = 1111;
        if ($key === $key_key) {
            echo 'パスワードは一致している';
        } else {
            echo 'パスワードは一致していない';
        }
        echo '<br>';

// <!-- ⑥if命令を使ってテストの点数を評価しなさい。100点なら「上級」、80点以上なら「中級」、60点以上なら「初級」、それ以外は「追試」とする。 -->
        $test = 85;
        if ($test == 100) {
            echo '上級';
        } elseif ($test >= 80) {
            echo '中級';
        } elseif ($test >= 60) {
            echo '初級';
        } else {
            echo '追試';
        }
        echo '<br>';

// <!-- ⑦値が偶数の場合、奇数の場合、0以下の場合を判断し、その結果を表示しなさい。
// 実行イメージ　　（値が10の場合）10：偶数　（値が15の場合）15：奇数　（値が0以下の場合）0：0より大きい値を設定してください -->
        $num = -10;
        if ($num > 0 && $num % 2 == 0) {
            $message = '偶数';
            echo "{$num}：{$message}";
        } elseif ($num > 0 && $num % 2 == 1) {
            $message = '奇数';
            echo "{$num} ：{$message}";
        } elseif ($num <= 0) {
            $message = '0より大きい値を設定してください';
            echo "{$num}：{$message}";
        }
        echo '<br>';

        $num = -10;
        if ($num > 0){
            if ($num % 2 == 0) {
            echo $num .'：偶数';
        }  else {
            echo $num .'：奇数';
        }
        } else {
            echo $num .'0より大きい値を設定してください';
        }
        echo '<br>';

// <!-- ⑧配列$argsに文字列'10'と'20'を代入しなさい。また、配列の文字列を数値に型変換（型キャスト）させて、計算結果を表示しなさい。※1行目「$args = [];」の続き2行目から記述すること。
// 実行イメージ　　10+20=30 -->
        $args = [];
        $args[0] = '10';
        $args[1] = '20';
        (int)$args[0];
        (int)$args[1];
        $result = $args[0] + $args[1];
        echo "{$args[0]}+{$args[1]}={$result}";
    ?>
</body>
</html>