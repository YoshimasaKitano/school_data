<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php $num =7;?>
    <?php $added = ++$num; ?>
    <p>前置インクリメント時のnum：<?=$num?></p>
    <p>前置インクリメント時のadded：<?=$added?></p>

    <?php $num =7;?>
    <?php $added = $num++; ?>
    <p>後置インクリメント時のnum：<?=$num?></p>
    <p>後置インクリメント時のadded：<?=$added?></p>
</body>
</html>