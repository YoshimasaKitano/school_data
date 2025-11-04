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
    // 【演習問題・3】

    // ⑨while命令を使って文字列を5回繰り返して表示しなさい。
        /* 実行イメージ
        　 PHP復習：1回目
        　 PHP復習：2回目
        　 PHP復習：3回目
        　 PHP復習：4回目
        　 PHP復習：5回目
        */
        $count = 1;
        while ($count < 6) {
            echo "PHP復習：{$count}回目";
            echo '<br>';
            $count += 1;
        }
        echo '<br>';

    // ⑩for命令とcount関数を使って、配列 [65, 40, 80, 33, 100] から最大値と最小値を取り出し表示しなさい。
        /* 実行イメージ
        最大値：100
        最小値：33
        */
        $num = [65, 40, 80, 33, 100];
        $min = 100;
        $max = 0;
        for ($i = 0; $i < count($num); $i++) {
            if ($min > $num[$i]) {
                $min = $num[$i];
            }
            if ($max < $num[$i]) {
                $max = $num[$i];
            }
        }
        echo "最大値：{$max}";
        echo "最小値：{$min}";
        echo '<br>';

    // ⑪for命令とcontinue命令を使って、1～100までの奇数の合計を計算しなさい。
        // 実行イメージ　　奇数の合計値は〇〇です
        $result = 0;
        for ($i = 1; $i < 101; $i++) {
            if ($i % 2 == 0) {
                continue;
            } else {
                $result += $i;
            }
        }
        echo "奇数の合計値は{$result}です";
        echo '<br>';

    // ⑫foreach命令とリファレンス渡しを使って配列の値を一律に1.5倍に計算し表示しなさい。
        // 実行イメージ　　Array ( [0] => 15 [1] => 45 [2] => 90 )
        $nums = [10, 30, 60];
        foreach ($nums as &$num) {
            $num *= 1.5;
        }
        unset($num);
        print_r($nums);
        echo '<br>';

    // ⑬if命令と論理演算子を使って変数$languageの値が「HTML」、「CSS」、「JavaScript」であれば「クライアントが理解する言語」と表示し、「PHP」、「Python」であれば「サーバーが理解する言語」と表示しなさい。 
        $language = 'HTML';
            if ($language === 'HTML' || $language === 'CSS' || $language === 'JavaScript') {
                echo 'クライアントが理解する言語';
            } elseif ($language === 'PHP' || $language === 'Python') {
                echo 'サーバーが理解する言語';
            }
        echo '<br>';

    // ⑭連想配列$usersに値を代入しなさい。また、$keyと$valueを使って値を出力しなさい。
        /* 実行イメージ
        name - 山田
        age - 20
        address - 大阪
        */

        $users = [];
        $users['name'] = '山田';
        $users['age'] = 20;
        $users['address'] = '大阪';
        foreach ($users as $key => $value) {
            echo "<p>{$key} - {$value}</p>";
        }
    ?>
</body>
</html>