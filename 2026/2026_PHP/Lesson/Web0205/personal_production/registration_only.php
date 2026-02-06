<?php 
    declare(strict_types=1);
    require_once dirname(__FILE__) . '/functions.php';
?>
<?php if ($_SERVER['REQUEST_METHOD'] === 'GET'): ?>
    <!DOCTYPE html>
        <html lang="ja">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>単語の単一登録</title>
            <link rel="stylesheet" href="static/css/reset.css">
            <link rel="stylesheet" href="static/css/style.css">
        </head>
        <body>
            <h1>単語の単一登録</h1>
            <form action="registration_only_confirm.php" method="GET">
                <label>単語: <input type="text" name="vocabulary" required></label><br>
                <label>意味: <input type="text" name="mean" required></label><br>
                <label>カテゴリー: <input type="text" name="category"></label><br>
                <button type="submit" name="operation">登録</button>
            </form>
            <p><a href="index.html">戻る</a></p>
        </body>
        </html>
<?php else:
    session_start();
    if (!empty($_POST['category'])) {
        $categories = $_SESSION['category'];
        $categories[] = $_POST['category'];
        $categories = array_adjust($categories);
        $_SESSION['category'] = $categories;
    }
    try {
        $pdo = connect();
        $statement = $pdo->prepare('SELECT * FROM notebooks');
        $statement->execute();
    } catch (PDOException $e) {
        echo '検索に失敗しました。';
        return;
    }
    $rows_count = count($statement->fetchall(PDO::FETCH_ASSOC));
    try {
        $pdo = connect();
        $statement = $pdo->prepare("INSERT INTO notebooks(vocabulary, mean, category, index_number) VALUES(:vocabulary, :mean, :category, :index_number)");
        $statement->bindValue(':vocabulary', $_POST['vocabulary'], PDO::PARAM_STR);
        $statement->bindValue(':mean', $_POST['mean'], PDO::PARAM_STR);
        $statement->bindValue(':category', $_POST['category'], PDO::PARAM_STR);
        $statement->bindValue(':index_number', $rows_count, PDO::PARAM_INT);
        $statement->execute();
    } catch (PDOException $e) {
        echo '登録に失敗しました。';
        return;
    }
    header('Location: index.html');
?>
<?php endif; ?>