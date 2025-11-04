<?php declare(strict_types=1); ?>
<body>
<?php

    // ユーザが入力したフリーワード。A.T.車(オートマ車)の本を探したい。
    $freeWord = 'A.T.';

    $books = [
        'A.T.車の運転マナー',
        '0AuthによるWebサービス認証入門',
        '睡眠は枕で変わる'
    ];

    echo '●エスケープなしで本を検索する例', PHP_EOL;
    foreach ($books as $book) {
        if (preg_match("/{$freeWord}/ui", $book)) {
            echo '・ヒットした本のタイトル：', $book, PHP_EOL; // 「0Auth」という単語まで引っかかってしまう
        }
    }

    echo '●エスケープして本を検索する例', PHP_EOL;
    foreach ($books as $book) {
        if (preg_match('/' .preg_quote($freeWord, '/') .'/ui', $book)) {
            echo '・ヒットした曲のタイトル：', $book, PHP_EOL;
        }
    }
?>
</body>