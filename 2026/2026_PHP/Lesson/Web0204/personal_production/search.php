<?php declare(strict_types=1); ?>

<?php
    require_once dirname(__FILE__) . '/functions.php';

    try {
        $pdo = connect();
        $statement = $pdo->prepare('SELECT vocabulary, mean, category from notebooks');
        $statement->execute();
    } catch (PDOException $e) {
        echo '単語帳の検索に失敗しました。';
        return;
    }
    $row = $statement->fetchall(PDO::FETCH_ASSOC);
?>
<?php if (!empty($row)): ?>
    <!DOCTYPE html>
    <html lang="ja">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>単語帳一覧</title>
    </head>
    <body>
        <h1>単語帳一覧</h1>
        <table border="1">
            <tr>
                <th>単語名</th>
                <th>単語の意味</th>
                <th>単語のカテゴリー</th>
                <th>更新</th>
                <th>削除</th>
            </tr>
            <?php for ($i = 0; $i < count($row); $i++): ?>
                <tr>
                    <td><?= $row[$i]['vocabulary']; ?></td>
                    <td><?= $row[$i]['mean']; ?></td>
                    <td><?= $row[$i]['category']; ?></td>
                    <td>
                        <form action="update.php" method="GET">
                            <button type="submit" name="update_operation" value="<?= $i; ?>">更新</button>
                        </form> 
                    </td>
                    <td>
                        <form action="delete_confirm.php" method="GET">
                            <button type="submit" name="delete_operation" value="<?= $i; ?>">削除</button>
                        </form>
                    </td>
                </tr>
            <?php endfor; ?>
        </table>
        <p><a href="index.html">戻る</a></p>
    </body>
    </html>
<?php else: ?>
    <!DOCTYPE html>
    <html lang="ja">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>単語帳一覧</title>
    </head>
    <body>
        <h1>単語帳一覧</h1>
        <h2>単語が登録されていません。</h2>
        <p><a href="index.html">戻る</a></p>
    </body>
    </html>
<?php endif; ?>