<?php
    declare(strict_types=1);
    setcookie('name1', 'value1', time() + 60 * 60, '/', '', false, true);
    setcookie('name1', '', time() - 60 * 60, '/', '', false, true);
?>
<body>
    <p>PHPからクッキーを送出した後、すぐに削除しました。</p>
</body>