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

/**
 * 文字列の前後、文字列内の空白をすべて削除する関数
 */
function complete_space($string)
{
    $string = trim($string);
    $string = preg_replace('/\s+|[　]+/u', '', $string);
    return $string;
}

/**
 * 配列内の重複要素の削除と、インデックス番号を整える関数
 */
function array_adjust($array)
{
    $array = array_unique($array);
    $array = array_values($array);
    return $array;
}