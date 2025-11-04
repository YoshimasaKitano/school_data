<?php declare(strict_types=1); ?>
<body>
<?php
    echo '●flower.pngをコピーしてflower-copy1.pngを作ります。', PHP_EOL;
    copy('./files/flower.png', './files/flower-copy1.png');

    echo '●flower.pngをコピーしてflower-copy2.pngを作ります。', PHP_EOL;
    copy('./files/flower.png', './files/flower-copy2.png');

    echo '●flower.pngをコピーしてflower-copy3.pngを作ります。', PHP_EOL;
    copy('./files/flower.png', './files/flower-copy3.png');

    echo '●flower-copy1.pngをflower-rename1.pngにリネームします。', PHP_EOL;
    copy('./files/flower-copy1.png', './files/flower-rename1.png');

    echo '●flower-copy2.pngを削除します。', PHP_EOL;
    unlink('./files/flower-copy2.png');
?>
</body>