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
        function add($a, $b)
        {
            if ($a <= 0) {
                echo '引数aは正の数で指定してください。';
                return;
            }
            if ($b <= 0) {
                echo '引数bは正の数で指定してください。';
                return;
            }
            $total = $a + $b;
            echo '合計は', $total;
            return $total;
        }

        $total = add(-5, 5);
        echo $total;
    ?>
</body>
</html>