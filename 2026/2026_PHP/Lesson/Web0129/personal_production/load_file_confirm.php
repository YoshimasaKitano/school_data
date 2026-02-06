<?php 
    declare(strict_types=1); 
    require_once dirname(__FILE__) . '/functions.php';
?>
<?php
    if ($_SERVER['REQUEST_METHOD'] === 'POST') {
        try{
            $pdo = connect();
            $statement = $pdo->prepare('SELECT * FROM notebooks');
            $statement->execute();
        } catch (PDOException $e) {
            echo '検索に失敗しました。';
        }
        $row_count = count($statement->fetchall(PDO::FETCH_ASSOC));

        $vocabulary_list = file($_FILES['upload']['tmp_name']);
        for ($i = 0; $i < count($vocabulary_list); $i++) {
            $vocabulary = complete_space($vocabulary_list[$i]);
            if (mb_substr($vocabulary, 0, 1) == '◎') {
                try {
                    $pdo = connect();
                    $statement = $pdo->prepare('INSERT INTO notebooks(vocabulary, index_number) VALUES(:vocabulary, :index_number)');
                    $statement->bindValue(':vocabulary', mb_substr($vocabulary, 1, mb_strlen($vocabulary)), PDO::PARAM_STR);
                    $statement->bindValue(':index_number', $row_count, PDO::PARAM_INT);
                    $row_count ++;
                    $statement->execute();
                } catch (PDOException $e) {
                    echo '単語登録に失敗しました。';
                    return;
                }    
            } elseif (mb_substr($vocabulary, 0, 1) == '〇') {
                $vocabulary_before = complete_space($vocabulary_list[$i - 1]);
                try {
                    $pdo = connect();
                    $statement = $pdo->prepare('UPDATE notebooks SET mean = :mean WHERE vocabulary = :vocabulary');
                    $statement->bindValue(':mean', mb_substr($vocabulary, 1, mb_strlen($vocabulary)));
                    $statement->bindValue(':vocabulary', mb_substr($vocabulary_before, 1, mb_strlen($vocabulary_before)));
                    $statement->execute();
                } catch (PDOException $e) {
                    echo '単語の意味登録に失敗しました。';
                    return;
                }
            }
        }
        try {
            $pdo = connect();
            $statement = $pdo->prepare('SELECT vocabulary, mean, category from notebooks');
            $statement->execute();
        } catch (PDOException $e) {
            echo '単語帳の検索に失敗しました。';
            return;
        }
        $row = $statement->fetchall(PDO::FETCH_ASSOC);
    }
?>
    <!DOCTYPE html>
    <html lang="ja">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>ファイルから単語の登録</title>
    </head>
    <body>
        <h1>登録確認</h1>
        <h2>ファイルから単語を追加し、単語帳は以下の通りになりました。</h2>
        <table border="1">
            <tr>
                <th>単語名</th>
                <th>単語の意味</th>
                <th>単語のカテゴリー</th>
            </tr>
            <?php for ($i = 0; $i < count($row); $i++): ?>
                <tr>
                    <td><?= $row[$i]['vocabulary']; ?></td>
                    <td><?= $row[$i]['mean']; ?></td>
                    <td><?= $row[$i]['category']; ?></td>
                </tr>
            <?php endfor; ?>
        </table>
        <p><a href="load_file.html">戻る</a></p>
    </body>
    </html>

