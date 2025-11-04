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
        $airports = [
            [
                'name'      => '羽田',
                'address'   => '東京都大田区'
            ],
            [
                'name'      => '成田',
                'address'   => '千葉県成田市'
            ],
            [
                'name'      => '中部国際',
                'address'   => '愛知県常滑市'
            ]
        ];

        // 空港を追加
        $airports[] =
        [
            'name'          => '関西国際',
            'address'       => '大阪府泉佐野市'
        ];
    ?>
    <p><?=$airports[0]['name']?> - <?=$airports[0]['address']?></p>
    <p><?=$airports[1]['name']?> - <?=$airports[1]['address']?></p>
    <p><?=$airports[2]['name']?> - <?=$airports[2]['address']?></p>
    <p><?=$airports[3]['name']?> - <?=$airports[3]['address']?></p>
    <p><pre><?php print_r($airports);?></ple></p>
</body>
</html>