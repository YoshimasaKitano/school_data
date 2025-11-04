<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php
        // 年齢をもとめる関数
        function calculateAge($today, $birthday)
        {
            $total = floor(($today - $birthday) / 10000);
            return $total;
        }
        // KDをもとめる関数
        function kd($kill, $death)
        {
            $ans = floor(($kill / $death) * 100);
            $ans /= 100;
            return $ans;
        }
        // 岡本篤希が学校を休む確率を求める関数
        function absent($toukoubi, $kesseki)
        {
            $result = floor(($kesseki / $toukoubi) * 100 + 100);
            return $result;
        }

        $age = calculateAge(20250723, 20060818);
        echo "{$age}歳";
        echo '<br>';

        $killDeath = kd(4, 3);
        echo "あなたのKDは{$killDeath}です。";
        echo '<br>';

        $okamoto = absent(90, 0);
        echo "お前の欠席確率は{$okamoto}%^^";
    ?>
</body>
</html>