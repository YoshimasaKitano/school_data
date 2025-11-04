<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello World - honkaku</title>
</head>
<body>
    <?php $total = 500 * 1.1 ?>
    <p>税込金額は<?php echo $total; ?>円です。</p>
    <p>税込金額は<?php print $total; ?>円です。</p>
    <p>税込金額は<?=$total?>円です。</p>
    <p><?php echo '税込金額は', $total, '円です。'?></p>
    <p><?php print '税込金額は' . $total . '円です。'?></p>
    <p><?='税込金額は', $total, '円です。'?></p>
</body>
</html>