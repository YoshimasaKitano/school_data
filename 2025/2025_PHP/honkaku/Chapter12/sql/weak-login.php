<?php
    /* 注意：本プログラムは脆弱性を含みます。 */
    declare(strict_types=1);

    // DBに接続する関数
    function connect(): PDO
    {
        $pdo = new PDO('mysql:host=localhost; dbname=honkaku; charset=utf8mb4', 'root', "");
    }