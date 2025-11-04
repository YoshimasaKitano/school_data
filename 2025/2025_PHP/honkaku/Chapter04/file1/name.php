<?php declare(strict_types=1); ?>
<body>
<?php
    echo '●相対パスでファイルを指定した場合', PHP_EOL;
    $filePath = './files/dir2/file.txt';
    echo 'ファイル名：', basename($filePath), PHP_EOL;
    echo 'ファイル名(拡張子なし)：', basename($filePath, '.txt'), PHP_EOL;
    echo 'ディレクトリ名：', dirname($filePath), PHP_EOL;
    echo 'ディレクトリ名(2階層上)：', dirname($filePath, 2), PHP_EOL;
    echo '絶対パス：', realpath($filePath), PHP_EOL;
    echo '拡張子：', pathinfo($filePath, PATHINFO_EXTENSION),PHP_EOL;
    echo 'ファイル名：', pathinfo($filePath, PATHINFO_FILENAME), PHP_EOL;

    echo '●絶対パスでファイルを指定した場合', PHP_EOL;
    $filePath = 'C:\xampp7\htdocs\chapter04\file1\files\dir1\dir2\file.txt;';
    echo 'ファイル名：', basename($filePath), PHP_EOL;
    echo 'ディレクトリ名：', dirname($filePath), PHP_EOL;
    echo '絶対パス：', realpath($filePath), PHP_EOL;
    echo '拡張子：', pathinfo($filePath, PATHINFO_EXTENSION), PHP_EOL;
?>
</body>