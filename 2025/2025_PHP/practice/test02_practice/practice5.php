<?php
    function connect(): PDO
    {
        $pdo = new PDO('mysql:host=localhost; dbname=〇〇; charset=utf8mb4', 'root', '');
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        $pdo->setAttribute(PDO::ATTR_EMULATE_PREPARES, false);
        return $pdo;
    }