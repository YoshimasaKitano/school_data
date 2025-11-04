<?php
session_start();

// 直前のエラーと入力値(フラッシュ)を取り出す。なければ初期値
if (isset($_SESSION['errors'])) {
    $errors = $_SESSION['errors'];
} else {
    $errors = [];
}
if (isset($_SESSION['form_data'])) {
    $form_data = $_SESSION['form_data'];
} else {
    $form_data = [
        'name' => '',
        'email' => '',
        'comment' => '',
        'agree' => '' // '1' ならチェック済み
    ];
}

// フラッシュ=「次の1回だけ使うセッション」
// 使い方=保存 → リダイレクト → 表示 → すぐ削除
// 成功メッセージ(1回だけ表示するフラッシュ)
if (isset($_SESSION['flash_success'])) {
    $flash_success = $_SESSION['flash_success'];
} else {
    $flash_success =  '';
}

// フラッシュは取り出したら破棄(次のリロードで残らないように)
unset($_SESSION['errors'], $_SESSION['form_data'], $_SESSION['flash_success']);

// 出力専用：xss対策(HTMLエスケープ)
// $s=関数に渡される引数(パラメータ)、stringのs
function h($s) { return htmlspecialchars($s, ENT_QUOTES, 'UTF-8' ); }

?>
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <!-- <meta http-equiv="X-UA-Compatible" content="IE=edge"> -->
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>お問い合わせフォーム</title>
</head>
<body>

    <?php if ($flash_success !== ''): ?>
        <div class="flash-success"><?= h($flash_success); ?></div>
    <?php endif; ?>

    <h1>お問い合わせフォーム</h1>
    <form action="process.php" method="POST">
        <p><label>名前：<input type="text" name="name" value="<?= h($form_data['name']); ?>"></label></p>
        <?php if (isset($errors['name'])): ?>
        <span class="error"><?= h($errors['name']); ?></span>
        <?php endif; ?>

        <p><label>メールアドレス：<input type="email" name="email" value="<?= h($form_data['email']); ?>"></label></p>
        <?php if (isset($errors['email'])): ?>
        <span class="error"><?= h($errors['email']); ?></span>
        <?php endif; ?>

        <p><label>コメント(ご意見・ご要望など) ：<textarea name="comment"><?= h($form_data['comment']); ?></textarea></label></p>
        <?php if (isset($errors['comment'])): ?>
        <span class="error"><?= h($errors['comment']); ?></span>
        <?php endif; ?>

        <p><label><input type="checkbox" name="agree" value="1" <?php if ($form_data['agree'] === '1') { echo 'checked'; }?>>利用規約に同意します</label></p>
        <?php if (isset($errors['agree'])): ?>
        <span class="error"><?= h($errors['agree']); ?></span>
        <?php endif; ?>

        <p><button type="submit">送信する</button></p>

    </form>
</body>
</html>