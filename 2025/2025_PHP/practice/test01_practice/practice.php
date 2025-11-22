<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php
        $name = '北野善聖';
        
        echo '私の名前は' .$name .'です。';
        echo '<br>';

        echo '私の名前は', $name, 'です。';
        echo '<br>';

        echo "私の名前は{$name}です。";
        echo '<br>';

        $num1 = 10;
        $num2 = 20;
        $num3 = 30;
        $result = 0;

        $result = $num1 + $num2 + $num3;

        echo "加算結果：{$result}";
        echo '<br>';

        define('TAX', 0.1);

        $total = 1000 * TAX + 1000;

        echo "税込み{$total}円";
        echo '<br>';

        $fruits = [];
        $fruits[0] = 'apple';
        $fruits[1] = 'orange';
        $fruits[2] = 'lemon';
        print_r($fruits);
        echo '<br>';

        $password1 = 12345;
        $password2 = 67890;

        if ($password1 === $password2) {
            echo 'パスワードは一致している';
        } else {
            echo 'パスワードは一致していない';
        }
        echo '<br>';

        $test = 35;
        if ($test == 100) {
            echo '上級';
        } elseif ($test >= 80) {
            echo '中級';
        } elseif ($test >= 60) {
            echo '初級';
        } else {
            echo '追試';
        }
        echo '<br>';

        $num = -10;
        if ($num > 0) {
            if ($num % 2 == 0) {
                echo "{$num}：偶数";
            } else {
                echo "{$num}：奇数";
            }
        } else {
            echo "{$num}：0より大きい値を設定してください";
        }
        echo '<br>';

        $args = [];
        $args[0] = '10';
        $args[1] = '20';
        $args1 = (int)$args[0];
        $args2 = (int)$args[1];
        $total = $args1 + $args2;
        echo "{$args1} + {$args2} = {$total}";
        echo '<br>';

        $i = 1;
        while ($i < 6) {
            echo "PHP復習：{$i}回目";
            echo '<br>';
            $i += 1;
        }

        $nums = [65, 40, 80, 33, 100];
        $min = $nums[0];
        $max = $nums[0];
        for ($i = 1; $i < count($nums); $i++) {
            if ($min > $nums[$i]) {
                $min = $nums[$i];
            }
            if ($max < $nums[$i]) {
                $max = $nums[$i];
            }
        }
        echo "最大値：{$max}";
        echo '<br>';
        echo "最小値：{$min}";
        echo '<br>';

        $result = 0;
        for ($i = 1; $i <101; $i++) {
            if ($i % 2 == 0) {
                continue;
            }
            $result += $i;
        }
        echo "奇数の合計値は{$result}です";
        echo '<br>';
        
        $nums =[10, 30, 60];
        foreach ($nums as &$num) {
            $num *= 1.5;
        }
        unset($num);
        print_r($nums);
        echo '<br>';

        $language = 'HTML';
        if ($language == 'HTML' || $language == 'CSS' || $language == 'JavaScript') {
            echo 'クライアントが理解する言語';
        } elseif ($language == 'PHP' || $language == 'Python') {
            echo 'サーバーが理解する言語';
        }
        echo '<br>';

        $users = [];
        $users['name'] = '山田';
        $users['age'] = 20;
        $users['address'] = '大阪';
        foreach ($users as $key => $value) {
            echo "{$key} - {$value}<br>";
        }
    ?>
</body>
</html>