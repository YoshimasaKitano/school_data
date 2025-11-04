<body>
<?php
    // 前後にスペースがある文字列をトリムする
    $greeting = 'こんにちは';
    var_dump(trim($greeting));

    // 前後にスペース・タブ・改行コードがある文字列をトリムする
    $greeting = "こんにちは\t\r\n";
    var_dump(trim($greeting));
?>
</body>