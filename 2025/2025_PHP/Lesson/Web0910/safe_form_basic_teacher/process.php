<?php
session_start();

// POST以外はフォームへ戻す
if (!isset($_SERVER['REQUEST_METHOD']) || $_SERVER['REQUEST_METHOD'] !== 'POST') {
    header('Location: form.php');// リダイレクト
    exit;
}

// 未定義対策しながら値を取得（入力時はエスケープ不要：出力時のみ h()）
if (isset($_POST['name']))    { $name = $_POST['name']; }     else { $name = ''; }
if (isset($_POST['email']))   { $email = $_POST['email']; }   else { $email = ''; }
if (isset($_POST['comment'])) { $comment = $_POST['comment']; } else { $comment = ''; }
if (isset($_POST['agree']))   { $agree = $_POST['agree']; }   else { $agree = ''; }

$errors = [];

// バリデーション
// 名前：必須 / 50文字以内 / 文字種チェック（記号ブロック）
if ($name === '') {
    $errors['name'] = '名前を入力してください。';
} elseif (mb_strlen($name) > 50) {
    $errors['name'] = '名前は50文字以内で入力してください。';
} elseif (!preg_match('/^[ぁ-んァ-ン一-龥a-zA-Z0-9\s]+$/u', $name)) {
    // ひらがな・カタカナ・漢字・英数字・スペースのみ許可
    $errors['name'] = '名前に使用できない文字が含まれています。';
}

// メール：必須 / 形式
if ($email === '') {
    $errors['email'] = 'メールアドレスを入力してください。';
} elseif (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
    $errors['email'] = 'メールアドレスの形式が正しくありません。';
}

// コメント：必須 / 最大1000文字
if ($comment === '') {
    $errors['comment'] = 'コメントを入力してください。';
} elseif (mb_strlen($comment) > 1000) {
    $errors['comment'] = 'コメントは1000文字以内で入力してください。';
}

// 規約同意：必須（チェックされてないと $_POST['agree'] は未定義）
if ($agree !== '1') {
    $errors['agree'] = '利用規約に同意してください。';
}

// エラーがあれば form.php へ戻す（エラー・入力値をフラッシュ保存）
if ($errors) {
    $_SESSION['errors'] = $errors;
    $_SESSION['form_data'] = [
        'name'    => $name,
        'email'   => $email,
        'comment' => $comment,
        'agree'   => $agree
    ];
    header('Location: form.php');
    exit;
}

// 成功：成功メッセージをフラッシュ保存してform.phpに戻す
$_SESSION['flash_success'] = '登録しました';
header('Location: form.php');
exit;
