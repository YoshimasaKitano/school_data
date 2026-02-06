<?php declare(strict_types=1); ?>

<!-- 関数を定義するファイル -->

<?php
/**
 * PDOインスタンスを取得する関数
 */
function connect(): PDO
{
    $pdo = new PDO('mysql:host=localhost; dbname=vocabulary_notebook; charset=utf8mb4', 'root', '');
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    $pdo->setAttribute(PDO::ATTR_EMULATE_PREPARES, false);
    return $pdo;
}