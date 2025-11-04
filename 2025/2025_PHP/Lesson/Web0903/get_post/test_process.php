<?php

// 1.POST送信かどうか確認
// 「存在しなければ」、「リクエストがPOSTではない場合」
if (!isset($_SERVER['REQUEST_METHOD']) || $_SERVER['REQUEST_METHOD'] !== 'POST') {
    echo 'これはPOST送信ではありません。URL直打ちやGETアクセスです。';
    echo '<a href="test_form.html">フォームに戻る</a>';
    exit;
}

// 2.値を取得
if (isset($_POST['name'])) {
    $name = $_POST['name'];    
} else {
    $name = '';
}

// 3.空欄チェック
if ($name === '') {
    echo 'POST送信はされましたが、名前が空欄です。';
    echo '<a href="test_form.html">フォームに戻る</a>';
    exit;
}

// 4.正常入力
echo '正常に入力されました！';
echo '入力された名前：' .htmlspecialchars($name, ENT_QUOTES, 'UTF-8');

// ----------------------------------------------------------------------

// セッション
// 値を持ちまわることができる
session_start();
// POST以外のアクセスはtest_form.htmlにリダイレクトで戻す
if (!isset($_SERVER['REQUEST_METHOD']) || $_SERVER['REQUEST_METHOD'] !== 'POST') {
    header('Location: test_form.html'); // リダイレクト
    exit;
}

// 2.値を取得
if (isset($_POST['name'])) {
    $name = $_POST['name'];    
} else {
    $name = '';
}

// バリデーション
$errors = [];
if ($name === '') {
    $errors['name'] = '名前を入力してください';
}

// エラーがある場合
if ($errors) {
    $_SESSION['errors'] = $errors;
}