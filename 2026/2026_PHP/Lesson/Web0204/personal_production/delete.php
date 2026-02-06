<?php declare(strict_types=1); ?>

<?php
    require_once dirname(__FILE__) . '/functions.php';

    try {
        $pdo = connect();
        $statement = $pdo->prepare('DELETE FROM notebooks WHERE vocabulary = :vocabulary');
        $statement->bindValue(':vocabulary', $_POST['vocabulary'], PDO::PARAM_STR);
        $statement->execute();
    } catch (PDOException $e) {
        echo '削除に失敗しました。';
        return;
    }
    try{
        $pdo = connect();
        $statement = $pdo->prepare('SELECT * FROM notebooks');
        $statement->execute();
    } catch (PDOException $e) {
        echo '検索に失敗しました。';
        return;
    }
    $rows = $statement->fetchall(PDO::FETCH_ASSOC);
    $i = 0;
    foreach ($rows as $row) {
        try {
            $pdo = connect();
            $statement = $pdo->prepare('UPDATE notebooks SET index_number = :index_number WHERE vocabulary = :vocabulary');
            $statement->bindValue(':index_number', $i - $stock, PDO::PARAM_INT);
            $statement->bindValue(':vocabulary', $row['vocabulary'], PDO::PARAM_STR);
            $statement->execute();
        } catch (PDOException $e) {
            echo '番号の上書きに失敗しました。';
            return;
        }
        $i++;
    }
    header('Location: search.php');
?>
