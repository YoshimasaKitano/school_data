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
        /* 正の整数であればtrue、そうでなければfalseを返す関数 */
        function checkNumber($value)
        {
            return is_numeric($value) && (int)$value > 0;
        }

        /* 2つの整数を足し算して返す関数　*/
        function add($a, $b)
        {
            if (checkNumber($a) || checkNumber($b)) {
                return 'INVALID';
            }
            $total = $a + $b;
            return $total;
        }

        // メインルーチン
        $result = add(3,10);
        echo "<p>計算結果：{$result}</p>";

        $result = add(5, -4);
        echo "<p>計算結果：{$result}</p>";
    ?>
</body>
</html>