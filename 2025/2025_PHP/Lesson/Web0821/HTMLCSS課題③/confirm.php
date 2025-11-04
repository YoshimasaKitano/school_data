<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>OCAサファリパーク in OSAKA</title>
    <link rel="stylesheet" href="css/reset.css">
    <link rel="stylesheet" href="css/style.css">
    <link rel="shortcut icon" href="images/logo50.png">
    <script src="https://kit.fontawesome.com/6643e64c88.js" crossorigin="anonymous"></script>
    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.8.3/jquery.min.js"></script>
</head>
<body>
    <?php include(dirname(__FILE__) .'/files/header.html'); ?>
    <main>
        <h2>ご来場者プレゼント</h2>
        <div class="confirmmain">
            <h3>送信内容</h3>
            <p>お名前：<?php if (empty($_POST['name'])) {
                echo 'ユーザー名を入力してください。';
            } else {
                echo htmlspecialchars($_POST['name'], ENT_QUOTES, 'UTF-8');
            }?></p>
            <p>メールアドレス：<?php if (empty($_POST['email'])) {
                echo 'メールアドレスを入力してください。';
            } else {
                echo htmlspecialchars($_POST['email'], ENT_QUOTES, 'UTF-8');
            }?></p>
            <p>性別：<?php echo $_POST['gender']; ?></p>
            <p>一番好きな動物：<?php echo $_POST['animal']; ?></p>
            <p>コメント：<?php if (empty($_POST['comment'])) {
                echo 'コメントを入力してください。';
            } else {
                echo htmlspecialchars($_POST['comment'], ENT_QUOTES, 'UTF-8');
            }?></p>
            <h4>ご応募いただきありがとうございました。当選した方にはメールを<br>お送りしますので、お手続きをお願いいたします。</h4>
        </div>
    </main>
    <?php include(dirname(__FILE__) .'/files/footer.html'); ?>
    <script src="js/main.js"></script>
</body>
</html>