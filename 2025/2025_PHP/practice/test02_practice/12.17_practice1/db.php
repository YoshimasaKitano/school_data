<?php
    function connect(): PDO
    {
        $pdo = new PDO('mysql:host=localhost; dbname=text_practice; charset=utf8mb4', 'root', '');
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        $pdo->setAttribute(PDO::ATTR_EMULATE_PREPARES, false);
        return $pdo;     
    }

    function escape(?string $value)
    {
        return htmlspecialchars(strval($value), ENT_QUOTES | ENT_HTML5, 'UTF-8');
    }