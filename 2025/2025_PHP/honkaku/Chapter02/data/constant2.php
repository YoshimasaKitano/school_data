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
        function someFunction()
        {
            echo '現在の関数名は：', __FUNCTION__, 'です。<br>';
        }
        echo '現在のファイル名は：', __FILE__, 'です。<br>';
        echo '現在の行番号は：', __LINE__, 'です。<br>';
        echo '現在のディレクトリは：', __DIR__, 'です。<br>';
        someFunction();
    ?>
</body>
</html>