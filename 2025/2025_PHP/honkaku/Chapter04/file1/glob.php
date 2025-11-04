<?php declare(strict_types=1); ?>
<body>
<?php
    $files = glob('files/user-images/user1234-*.{jpg,jpeg,gif,png}', GLOB_BRACE);
    print_r($files);
?>
</body>