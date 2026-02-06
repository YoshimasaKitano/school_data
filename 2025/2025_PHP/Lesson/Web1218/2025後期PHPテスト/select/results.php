<?php

    declare(strict_types=1);

    require_once dirname(__FILE__) . '/functions.php';

    // メインルーチン
    if ($_SERVER['REQUEST_METHOD'] === 'GET') {
        try {
            $pdo = connect();
            $statement = $pdo->prepare('INSERT INTO tests(number, name, subject, score) VALUES(:number, :name, :subject, :score)');
            $statement->bindValue(':number', $_GET['number'], PDO::PARAM_STR);
            $statement->bindValue(':name', $_GET['name'], PDO::PARAM_STR);
            $statement->bindValue(':subject', $_GET['subject'], PDO::PARAM_STR);
            $statement->bindValue(':score', $_GET['score'], PDO::PARAM_STR);
            $statement->execute();
        } catch (PDOException $e) {
            echo '結果登録に失敗しました。';
            return;
        }
    } else {

        try {
            $pdo = connect();
            $statement = $pdo->prepare("SELECT subject, score FROM tests WHERE number = :number");
            $statement->bindValue(':number', $_POST['number'], PDO::PARAM_STR);
            $statement->execute();

        } catch (PDOException $e) {
            echo '検索に失敗しました。';
        }
        
        $row = $statement->fetchall(PDO::FETCH_ASSOC);

        // それぞれの得点

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

        if (!isset($english)) {
            $english = 0;
        }
        if (!isset($japan)) {
            $japan = 0;
        }
        if (!isset($math)) {
            $math = 0;
        }

        // 3教科の合計点
        $result = intval($english + $japan + $math);

        // 平均点
        $average = intval($english + $japan + $math) / 3;
    }
?>
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>検索結果</title>
    <link rel="stylesheet" href="css/reset.css">
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <?php if ($_SERVER['REQUEST_METHOD'] == 'GET'): ?>
        <h3>登録しました。</h3>
        <a href="./form.html">戻る</a>

    <?php elseif ($_SERVER['REQUEST_METHOD'] == 'POST'): ?>
        <h3><?=$_POST['number']; ?>のテスト結果</h3>
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