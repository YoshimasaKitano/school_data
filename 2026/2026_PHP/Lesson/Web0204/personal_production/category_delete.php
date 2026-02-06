<?php 
    declare(strict_types=1); 
    require_once dirname(__FILE__) . '/functions.php';
?>
<?php
    if ($_SERVER['REQUEST_METHOD'] === 'POST') {
        try {
            $pdo = connect();
            $statement = $pdo->prepare('SELECT vocabulary FROM notebooks WHERE category = :category');
            $statement->bindValue(':category', $_POST['category'], PDO::PARAM_STR);
            $statement->execute();
        } catch (PDOException $e) {
            echo '検索に失敗しました。';
            return;
        }
        $rows = $statement->fetchall(PDO::FETCH_ASSOC);
        foreach ($rows as $row) {
            try {
                $pdo = connect();
                $statement = $pdo->prepare('UPDATE notebooks SET category = :category WHERE vocabulary = :vocabulary');
                $statement->bindValue(':category', NULL, PDO::PARAM_STR);
                $statement->bindValue(':vocabulary', $row['vocabulary'], PDO::PARAM_STR);
                $statement->execute();
            } catch (PDOException $e) {
                echo '更新に失敗しました。';
                return;
            }
        }
        header('Location: category.php');
    }
?>