<?php declare(strict_types=1); ?>
<body>
    <a href="to.php?message=あ&い&う&え&お">URLエンコードしないリンク</a><br>
    <a href="to.php?message=<?=urlencode('あ&い&う&え&お')?>">URLエンコードしたリンク</a><br>
</body>