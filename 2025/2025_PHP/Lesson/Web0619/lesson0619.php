<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>lesson</title>
</head>
<body>
    <h1>演習</h1>
    <p>変数の使い方</p>
    <?php
    // 変数とは値を入れる入れ物
    // nameという名前の変数に「北野」という文字列を代入している
    // 変数には$マークをつける
    // イコールを使って右側の値を左の変数に代入
    // 変数の名前は意味の伝わるものにする
    $name = '北野';
    echo $name;
    echo '<br>';

    $num = 10;
    echo $num;
    echo '<br>';

    $num = '10';
    echo $num;
    echo '<br>';

    $sum = 10 + 10;
    echo $sum;
    echo '<br>';

    $sum = 123456788765434567 + 345678909876543;
    echo $sum;
    echo '<br>';

    // 私の名前は_です
    // ドットを使って連結
    $name = '北野善聖';
    echo '私の名前は' .$name .'です';
    echo '<br>';

    // カンマを使って次々出力
    $name = '北野善聖';
    echo '私の名前は', $name, 'です';
    echo '<br>';

    // 文字列の中で変数展開
    // シングルクォーテーションではなく、ダブルクォーテーションを使う
    $name = '北野善聖';
    echo "私の名前は{$name}です";
    echo '<br>';
    echo '私の名前は{$name}です';
    echo '<br>';




    ?>
</body>
</html>