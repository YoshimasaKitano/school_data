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
        $user = [
            'name'  => '山下次郎',
            'age'   => 30,
            'place' => '有田',
        ];
        $user['job']    = '伝統工芸士'; // 職業を追加
        $user['hobby']  = 'パン作り';   // 趣味を追加
    ?>
    <p><?=$user['name']?></p>
    <p><?=$user['age']?></p>
    <p><?=$user['place']?></p>
    <p><?=$user['job']?></p>
    <p><?=$user['hobby']?></p>
    <p><pre><?php print_r($user);?></ple></p>
</body>
</html>