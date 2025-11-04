<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
<pre>
<?php
    /* 三項演算子をもちいた例（1）*/
    $greeting = null;
    $message = $greeting === null ? 'Hello' : $greeting;
    echo 'あいさつは' .$message, PHP_EOL;

    /* 三項演算子をもちいた例（2）*/
    $greeting = 'Good Morning';
    $message = $greeting === null ? 'Hello' : $greeting;
    echo 'あいさつは' .$message, PHP_EOL;

    /* null合体演算子をもちいた例（1）*/
    $greeting = null;
    $message = $greeting ?? 'Hello';
    echo 'あいさつは' .$message, PHP_EOL;

    /* null合体演算子をもちいた例（2）*/
    $greeting = 'Good Morning';
    $message = $greeting ?? 'Hello';
    echo 'あいさつは' .$message, PHP_EOL;
?>
</body>
</html>