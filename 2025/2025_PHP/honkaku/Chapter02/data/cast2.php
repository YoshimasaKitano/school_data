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
        var_dump(strval(1234));      // string '1234'
        var_dump(intval(1234.5));    // int 1234
        var_dump(strval(true));      // string '1'
        var_dump(strval(false));     // string ''
        var_dump(boolval('true'));   // bool true
        var_dump(boolval('false'));  // bool true
        var_dump(boolval(0));        // bool false
        var_dump(boolval(1));        // bool true
        var_dump(boolval(-1));       // bool true
    ?>
</body>
</html>