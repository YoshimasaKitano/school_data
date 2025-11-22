<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php
        $numbers = [10, 20, 30, 40, 50];
        $result = 0;
        $average = 0;
        $result = $numbers[0] + $numbers[1] + $numbers[2] + $numbers[3] + $numbers[4];
        $average = $result / 5;
        echo "合計：{$result}";
        echo '<br>';
        echo "平均：{$average}";
        echo '<br>';

        $items = [
            "りんご" => 120,
            "バナナ" => 80,
            "みかん" => 100
        ];
        foreach ($items as $key => $value) {
            echo "{$key}は{$value}円です。<br>";
        }
        
        $students = [
            ["name" => "たろう", "math" => 80, "english" => 70],
            ["name" => "はなこ", "math" => 90, "english" => 85],
            ["name" => "じろう", "math" => 60, "english" => 75]
        ];
        $students[0]['result'] = $students[0]['math'] + $students[0]['english'];
        $students[1]['result'] = $students[1]['math'] + $students[1]['english'];
        $students[2]['result'] = $students[2]['math'] + $students[2]['english'];
        $students[0]['average'] = $students[0]['result'] / 2;
        $students[1]['average'] = $students[1]['result'] / 2;
        $students[2]['average'] = $students[2]['result'] / 2;
        for ($i = 0; $i < 3; $i++) {
            echo "{$students[$i]['name']}の合計:{$students[$i]['result']}, 平均:{$students[$i]['average']}";
            echo '<br>';
        }

        $students = [
            ["name" => "たろう", "math" => 80, "english" => 70],
            ["name" => "はなこ", "math" => 90, "english" => 85],
            ["name" => "じろう", "math" => 60, "english" => 75]
        ];
        foreach ($students as $student) {
            $result = $student['math'] + $student['english'];
            $average = $result / 2;
            echo "{$student['name']}の合計:{$result}, 平均:{$average}<br>";
        }

        $fruits = ["りんご", "バナナ", "みかん", "ぶどう"];
        $num = count($fruits);
        echo "フルーツの数は{$num}個です。";

        $items = [];
        if (count($items) == 0) {
            echo 'データがありません';
        } else {
            echo 'データがあります';
        }
        echo '<br>';

        $price = 1000;
        define('TAX', 0.1);
        $result = (TAX * $price) + $price;
        echo "税込価格は{$result}円です。";
        echo '<br>';

        $fruits1 = ["りんご", "バナナ"];
        $fruits2 = ["みかん", "ぶどう"];
        $fruits = array_merge($fruits1, $fruits2);
        foreach ($fruits as $fruit) {
            echo "{$fruit}<br>";
        }

        $a = ["name" => "たろう", "age" => 20];
        $b = ["age" => 25, "email" => "taro@example.com"];
        $merged1 = array_merge($a, $b);
        $merged2 = $a + $b;
        foreach ($merged1 as $merge1) {
            echo "{$merge1}<br>";
        }
        foreach ($merged2 as $merge2) {
            echo "{$merge2}<br>";
        }

        $numbers = [10, 20, 30];
        foreach ($numbers as &$number) {
            $number *= 2;
        }
        unset($number);
        foreach ($numbers as $number) {
            echo "{$number}<br>";
        }

        $score = 75;
        if ($score >= 80) {
            echo '優秀です';
        } elseif ($score >= 60) {
            echo '合格です';
        } else {
            '再試験です';
        }
        echo '<br>';

        $day = '月曜';
        switch($day) {
            case '月曜':
                echo '週の始まりです。';
                break;
            case '金曜':
                echo '明日は休みです。';
                break;
            case '土曜':
            case '日曜':
                echo '休日です。';
                break;
            default :
                echo '平日です。';
        }
        echo '<br>';

        $menu = 'カレー';
        switch($menu) {
            case 'カレー':
                echo 'カレーは500円です';
                break;
            case 'ラーメン':
                echo 'ラーメンは600円です';
                break;
            case 'サンドイッチ':
                echo 'サンドイッチは400円です';
                break;
            default :
                echo 'そのメニューは扱っていません';
        }
        echo '<br>';

        $filename = 'test.txt';
        if (!file_exists($filename)) {
            exit('ファイルが見つかりません');
        }
        echo "ファイルがあります";
        echo '<br>';

        $nums = [10, 20, 30];
        echo '<pre>';
        print_r($nums);
        echo '</pre>';

</body>
</html>