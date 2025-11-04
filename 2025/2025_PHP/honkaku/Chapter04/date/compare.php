<?php declare(strict_types=1); ?>
<body>
<?php
    $date1 = new DateTime('2019-02-25 09:23:00');
    $date2 = new DateTime('2019-02-25 17:12:34');

    var_dump($date1 == $date2); // 結果：false
    var_dump($date1 > $date2); // 結果：false
    var_dump($date1 >= $date2); // 結果：false
    var_dump($date1 < $date2); // 結果：true
    var_dump($date1 <= $date2); // 結果：true
?>
</body>