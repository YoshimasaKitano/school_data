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
        $quoted1 = 'The Book of "PHP\'s Honkaku"';
        $quoted2 = "The Book of \"PHP's Honkaku\"";
    ?>
    <p><?=$quoted1?></p>
    <p><?=$quoted2?></p>
</body>
</html>