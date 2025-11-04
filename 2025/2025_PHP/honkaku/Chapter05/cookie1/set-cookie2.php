<?php
    declare(strict_types=1);
    setcookie("name-as-array[0]", 'value0', time() + 60 * 60, '/', '', false, true);
    setcookie("name-as-array[1]", 'value1', time() + 60 * 60, '/', '', false, true);
    setcookie("name-as-array[2]", 'value2', time() + 60 * 60, '/', '', false, true);
?>
<body>
    <p>PHPからクッキーを送出しました</p>
</body>