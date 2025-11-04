1 <!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
<?php
    $temperature = 39; // 現在の水温は39℃です

    // 適温の範囲「内」であるかを調べる
    $isSuitable = $temperature >= 40 && $temperature <= 41;
    var_dump($isSuitable);      // 結果：false

    // 適温の範囲「外」であるかを調べる(1)
    $isNotSuitable = $temperature < 40 && $temperature > 41;
    var_dump($isnotSuitable);      // 結果：true

    // 適温の範囲「外」であるかを調べる(2)
    $isNotSuitable = !($temperature >= 40 && $temperature <= 41);
    var_dump($isNotSuitable);      // 結果：true
?>
</body>
</html>