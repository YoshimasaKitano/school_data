<?php declare(strict_types=1); ?>
<body>
<?php
    $books = file('books.txt');

    // books.txtの文字コードがShift-JISのため、以下のようにそのまま出力すると文字化けします。
    // var_dump($books);

    foreach ($books as $book) {
        // mb_convert_encodingで、1行ずつUTF-8に変換すると文字化けしません。
        echo mb_convert_encoding($book, 'UTF-8', 'SJIS-win'), PHP_EOL;
    }

    // または、mb_convert_variablesで、配列全体をUTF-8に変換することもできます。
    mb_convert_variables('UTF-8', 'SJIS-win', $books);
    foreach ($books as $book) {
        echo $book, PHP_EOL;
    }
?>
</body>