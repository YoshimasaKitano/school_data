<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello World - honkaku</title>
</head>
<body>
    <?php
        var_dump(1234);             // int 1234
        var_dump((string)1234);     // string '1234'
        var_dump((int)1234.5);      // int 1234
        var_dump((string)true);     // string '1'
        var_dump((string)false);    // string ''
        var_dump((bool)'true');     // bool true
        var_dump((bool)'false');    // bool true
        var_dump((bool)0);          // bool false
        var_dump((bool)1);          // bool true
        var_dump((bool)-1);         // bool true
    ?>
</body>
</html>