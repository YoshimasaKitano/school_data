<?php
    // XSS対策(出力時のみ使用)
    function h($str) {
        return htmlspecialchars($str, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8');
    }

    session_start();

    if (!isset($_POST["token"]) || $_POST["token"] != $_SESSION['token']) {
        echo "不正なリクエストです";
        exit();
    }


    // POST以外はフォームへ戻す
    if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
        header('Location: form_lesson.php');
        exit;
    }

    $name = empty($_POST['name']) ? '' : $_POST['name'];
    $email = empty($_POST['email']) ? '' : $_POST['email'];
    $tel = empty($_POST['tel']) ? '' : $_POST['tel'];
    $gender = empty($_POST['gender']) ? '' : $_POST['gender'];
    $animal = empty($_POST['animal']) ? '' : $_POST['animal'];
    $comment = empty($_POST['comment']) ? '' : $_POST['comment'];
    $agree = empty($_POST['agree']) ? '' : $_POST['agree'];

    if (empty($_POST['name'])) {
        $_SESSION['flash']['name'] = '<span style="color: red;">※お名前は必須項目です。</span>';
    } elseif (50 < mb_strlen($name, 'UTF-8')) {
        $_SESSION['flash']['name'] = '<span style="color: red;">※名前は50文字以内で入力してください。</span>';
    }
    $_SESSION['original']['name'] = $_POST['name'];

    if (empty($_POST['email'])) {
        $_SESSION['flash']['email'] = '<span style="color: red;">※メールアドレスは必須項目です。</span>';
    } elseif (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $_SESSION['flash']['email'] = '<span style="color: red;">※不正なメールアドレスの形式です。</span>';
    } elseif (30 < mb_strlen((string)$email, 'UTF-8')) {
        $_SESSION['flash']['email'] = '<span style="color: red;">※メールアドレスは30文字以内で入力してください。</span>';
    }
    $_SESSION['original']['email'] = $_POST['email'];

    if (empty($_POST['tel'])) {
        $_SESSION['flash']['tel'] = '<span style="color: red;">※電話番号は必須項目です。</span>';
    } elseif (!preg_match('/^\d{2,4}\d{2,4}\d{3,4}$/', $tel)) {
        $_SESSION['flash']['tel'] = '<span style="color: red;">※不正な電話番号の形式です。</span>';
    } elseif (13 < mb_strlen((string)$tel, 'UTF-8')) {
        $_SESSION['flash']['tel'] = '<span style="color: red;">※電話番号は13文字以内で入力してください。</span>';
    }
    $_SESSION['original']['tel'] = $_POST['tel'];

    if (empty($_POST['gender'])) {
        $_SESSION['flash']['gender'] = '<span style="color: red;">※性別は必須項目です。</span>';
    }
    $_SESSION['original']['gender'] = $_POST['gender'];

    if (empty($_POST['animal'])) {
        $_SESSION['flash']['animal'] = '<span style="color: red;">※好きな動物は必須項目です。</span>';
    }
    $_SESSION['original']['animal'] = $_POST['animal'];

    if (empty($_POST['comment'])) {
        $_SESSION['flash']['comment'] = '<span style="color: red;">※ご意見・ご感想は必須項目です。</span>';
    }
    $_SESSION['original']['comment'] = $_POST['comment'];

    if (empty($_POST['agree']) || $_POST['agree'] !== '1') {
        $_SESSION['flash']['agree'] = '<span style="color: red;">※個人情報保護方針への同意が必要です。</span>';
    }
    $_SESSION['original']['agree'] = $_POST['agree'];

    // 空欄 or 規約未同意ならフォームへリダイレクト
    if ($name === '' || $email === '' || $tel === ''|| $gender === '' || $animal === '' || $comment === '' || $agree === '' || 50 < mb_strlen($name, 'UTF-8') || !filter_var($email, FILTER_VALIDATE_EMAIL) || 30 < mb_strlen((string)$email, 'UTF-8') || !preg_match('/^\d{2,4}\d{2,4}\d{3,4}$/', $tel) || 13 < mb_strlen((string)$tel, 'UTF-8')){
        header('Location: form_lesson.php');
        exit;
    }

    // 空欄や未同意ならリダイレクトする処理の後に
    if ($name !== '' && $email !== '' && $tel !== '' && $gender !== '' && $animal !== '' && $comment !== '' && $agree !== '' ) {
    // セッションのエラー・入力値を消す
        unset($_SESSION['flash'], $_SESSION['original']);
    }

?>
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
            <p>お名前：<?=h($_POST['name']);?></p>
            <p>メールアドレス：<?=h($_POST['email']);?></p>
            <p>電話番号：<?=h($_POST['tel']);?></p>
            <p>性別：<?=h($_POST['gender']);?></p>
            <p>一番好きな動物：<?=h($_POST['animal']);?></p>
            <p class="comment">コメント：<?=h($_POST['comment']);?></p>
            <h4>ご応募いただきありがとうございました。当選した方にはメールを<br>お送りしますので、お手続きをお願いいたします。</h4>
        </div>
    </main>
    <?php include(dirname(__FILE__) .'/files/footer.html'); ?>
    <script src="js/main.js"></script>
</body>
</html>