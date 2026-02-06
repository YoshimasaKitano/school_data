<?php 
    declare(strict_types=1); 
    require_once dirname(__FILE__) . '/functions.php';
?>
<?php 
    if ($_SERVER['REQUEST_METHOD'] === 'GET') {
        session_start();
        $categories = [];
        $categories = $_SESSION['category'];
        $categories = array_adjust($categories);
    }
?>
<?php if ($_SERVER['REQUEST_METHOD'] === 'GET'): ?>
    <!DOCTYPE html>
    <html lang="ja">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>カテゴリー一覧</title>
        <link rel="stylesheet" href="static/css/reset.css">
        <link rel="stylesheet" href="static/css/style.css">
    </head>
    <body>
        <h1>カテゴリー一覧</h1>
        <?php if (!empty($categories)): ?>
            <table border="1">
                <tr>
                    <th>カテゴリーの名前</th>
                    <th>中身一覧</th>
                    <th>更新</th>
                    <th>削除</th>
                </tr>
                <?php foreach ($categories as $category): ?>
                    <tr>
                        <td><?= $category; ?></td>
                        <td>
                            <form action="content.php" method="GET">
                                <button type="submit" name="content_operation" value="<?= $category; ?>">中身</button>
                            </form> 
                        </td>
                        <td>
                            <form action="category_update.php" method="GET">
                                <button type="submit" name="category_update_operation" value="<?= $category; ?>">更新</button>
                            </form>
                        </td>
                        <td>
                            <form action="category_delete_confirm.php" method="GET">
                                <button type="submit" name="category_delete_operation" value="<?= $category; ?>">削除</button>
                            </form>
                        </td>
                    </tr>
                <?php endforeach; ?>
            </table>
        <?php else: ?>
            <h2>カテゴリーが存在しません</h2>
        <?php endif; ?>
        <h2><a href="make_category.php">カテゴリーを新規作成する</a></h2>
        <p><a href="index.html">戻る</a></p>
    </body>
    </html>
<?php endif; ?>