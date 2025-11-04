<?php declare(strict_types=1); ?>
<body>
<?php
    echo 'file関数でファイルを読み込みます。', PHP_EOL;
    $lines = file('files/note.txt');
    foreach ($lines as $line) {
        echo trim($line), PHP_EOL;
    }

    echo '●file-get_contents関数絵ファイルを読み込みます。', PHP_EOL;
    $contents = file_get_contents('files/note.txt');
    echo $contents, PHP_EOL;

    echo '●readfile関数でファイルを読み込みます。', PHP_EOL;
    readfile('files/note.txt');
?>
</body>