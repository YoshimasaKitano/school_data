<?php declare(strict_types=1); ?>

<!-- フォームから送られてきた得点をDBに格納する処理を行う
特定のユーザーの受けたテストの点数を検索し、点数、合計値、平均値を出力する処理を行う -->


<?php
    // function.phpを読み込み
    require_once dirname(__FILE__) . '/functions.php';

    // メインルーチン
    // プロトコルがGETの場合
    if ($_SERVER['REQUEST_METHOD'] === 'GET') {
        try {
            // DBに接続
            $pdo = connect();
            // フォームで送られてきた学籍番号、名前、テストの名前、教科名、点数をそれぞれプレースホルダーを作ってから後で代入していく
            $statement = $pdo->prepare('INSERT INTO tests(number, name, test, subject, score) VALUES(:number, :name, :test, :subject, :score)');
            $statement->bindValue(':number', $_GET['number'], PDO::PARAM_STR);
            $statement->bindValue(':name', $_GET['name'], PDO::PARAM_STR);
            $statement->bindValue(':test', $_GET['test'], PDO::PARAM_STR);
            $statement->bindValue(':subject', $_GET['subject'], PDO::PARAM_STR);
            $statement->bindValue(':score', $_GET['score'], PDO::PARAM_STR);
            $statement->execute();
        } catch (PDOException $e) {
            echo '結果登録に失敗しました。';
            return;
        }
    // プロトコルがPOSTの場合
    } else {
        try {
            // DBに接続
            $pdo = connect();
            // 特定のユーザーの学籍番号とテストの名前を用いて各教科の得点を検索する。プレースホルダーを作って後で代入していく。
            $statement = $pdo->prepare("SELECT subject, score FROM tests WHERE (number = :number) and (test = :test)");
            $statement->bindValue(':number', $_POST['number'], PDO::PARAM_STR);
            $statement->bindValue(':test', $_POST['test'], PDO::PARAM_STR);
            $statement->execute();

        } catch (PDOException $e) {
            echo '検索に失敗しました。';
        }
        
        // DBからとってきた内容をDBのカラム名がキーになった連想配列で変数$rowに代入
        $row = $statement->fetchall(PDO::FETCH_ASSOC);

        // それぞれの得点を連想配列のキーで指定してそれぞれの変数$english、$japan、$mathに代入
        for ($i = 0; $i < count($row); $i++) {
            if ($row[$i]['subject'] == 'English') {
                $english = $row[$i]['score'];
            } elseif ($row[$i]['subject'] == 'Japan') {
                $japan = $row[$i]['score'];
            } elseif ($row[$i]['subject'] == 'Math') {
                $math = $row[$i]['score'];
            }
        }

        // 入力されていないときの処理
        // カウンター領域の作成
        $count = 0;

        // 英語の得点が入力されていないとき
        if (!isset($english)) {
            $english = '-';
            $count++;
        }
        // 国語の得点が入力されてないとき
        if (!isset($japan)) {
            $japan = '-';
            $count += 3;
        }
        // 数学の点数が入力されていないとき
        if (!isset($math)) {
            $math = '-';
            $count += 5;
        }

        // カウンターの増やし方が1、3、5の理由
        // 1、2、3で増やしてしまうと、上記の処理を2つ以上行った場合、カウンターが足されて、1、2、3のどれかと被ってしまう可能性があり、被らないようにするため。

        // 上のどの処理が実行されたかによって合計値と平均値の処理が変わってくる

        // 3教科の合計点と平均点
        // 英語と国語と数学のデータがすべてあったとき
        if ($count == 0) {
            $result = intval($english + $japan + $math); // 英語と国語と数学の合計値
            $average = intval($english + $japan + $math) / 3; // 英語と国語と数学の平均値
        }
        // 国語と数学だけデータがあったとき
        elseif ($count == 1) {
            $result = intval($japan + $math); // 国語と数学の合計値
            $average = intval($japan + $math) / 2; // 国語と数学の平均値
        }
        // 英語と数学だけデータがあったとき
        elseif ($count == 3) {
            $result = intval($english + $math); // 英語と数学の合計値
            $average = intval($english + $math) / 2; // 英語と数学の平均値
        }
        // 数学だけデータがあったとき
        elseif ($count == 4) {
            $result = intval($math); // 数学単体の得点
            $average = intval($math); // 数学しかないので数学の得点が平均値となる
        }
        // 英語と国語だけデータがあったとき
        elseif ($count == 5) {
            $result = intval($english + $japan); // 英語と国語の合計値
            $average = intval($english + $japan) / 2; // 英語と国語の平均値
        }
        // 国語だけデータがあったとき
        elseif ($count == 6) {
            $result = intval($japan); // 国語単体の得点
            $average = intval($japan); // 国語しかないので国語の得点が平均値となる
        }
        // 英語だけデータがあったとき
        elseif ($count == 8) {
            $result = intval($english); // 英語単体の得点
            $average = intval($english); // 英語しかないので英語の得点が平均値となる
        }
        // どの教科のデータもなかったとき
        else {
            $result = '-'; // どの教科の点数も入っていないので-となる
            $average = '-'; // どの教科の点数も入っていないので-となる
        }
    }
?>
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>検索結果</title>
</head>
<body>
    <?php if ($_SERVER['REQUEST_METHOD'] == 'GET'): ?>
        <h3>登録しました。</h3>
        <a href="./form.html">戻る</a>

    <?php elseif ($_SERVER['REQUEST_METHOD'] == 'POST'): ?>
        <h3><?=$_POST['number']; ?>の<?=$_POST['test']; ?>の結果</h3>
        <table border="1">
            <tr>
                <th>英語</th>
                <th>国語</th>
                <th>数学</th>
                <th>合計点</th>
                <th>平均点</th>
            </tr>
                <tr>
                    <td><?=$english; ?></td>
                    <td><?=$japan; ?></td>
                    <td><?=$math; ?></td>
                    <td><?=$result; ?></td>
                    <td><?=$average; ?></td>
                </tr>
        </table>
        <a href="./form.html">戻る</a>
    <?php endif; ?>
</body>
</html>