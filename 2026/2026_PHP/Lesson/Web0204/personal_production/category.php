<?php 
    declare(strict_types=1); 
    require_once dirname(__FILE__) . '/functions.php';
?>
<?php 
    if ($_SERVER['REQUEST_METHOD'] === 'GET') {
        try {
            $pdo = connect();
            $statement = $pdo->prepare('SELECT vocabulary FROM notebooks WHERE not (category = "")');
            $statement->execute();
        } catch (PDOException $e) {
            echo '検索に失敗しました。';
            return;
        }
        $rows = $statement->fetchall(PDO::FETCH_ASSOC);
        foreach ($rows as $row) {
            try {
                $pdo = connect();
                $statement = $pdo->prepare('SELECT category FROM notebooks WHERE vocabulary = :vocabulary');
                $statement->bindValue(':vocabulary', $row['vocabulary'], PDO::PARAM_STR);
                $statement->execute();
            } catch (PDOException $e) {
                echo '検索に失敗しました。';
                return;
            }
        }
        $rows = $statement->fetchall(PDO::FETCH_ASSOC);
        $rows = array_unique($rows);
    }
?>
<?php if ($_SERVER['REQUEST_METHOD'] === 'GET'): ?>
    <!DOCTYPE html>
    <html lang="ja">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>カテゴリー一覧</title>
    </head>
    <body>
        <h1>カテゴリー一覧</h1>
        <?php if (!empty($row)): ?>
            <table border="1">
                <tr>
                    <th>カテゴリーの名前</th>
                    <th>中身一覧</th>
                    <th>更新</th>
                    <th>削除</th>
                </tr>
                <?php foreach ($rows as $row): ?>
                    <tr>
                        <td><?= $row['category']; ?></td>
                        <td>
                            <form action="content.php" method="GET">
                                <button type="submit" name="content_operation" value="<?= $row['category']; ?>">中身</button>
                            </form> 
                        </td>
                        <td>
                            <form action="category_update.php" method="GET">
                                <button type="submit" name="category_update_operation" value="<?= $row['category']; ?>">更新</button>
                            </form>
                        </td>
                        <td>
                            <form action="category_delete_confirm.php" method="GET">
                                <button type="submit" name="category_delete_operation" value="<?= $row['category']; ?>">削除</button>
                            </form>
                        </td>
                    </tr>
                <?php endforeach; ?>
            </table>
        <?php else: ?>
            <h2>カテゴリーが存在しません</h2>
        <?php endif; ?>
        <h2><a href="">カテゴリーを新規作成する</a></h2>
        <p><a href="index.html">戻る</a></p>
    </body>
    </html>
<?php endif; ?>