<?php
require_once __DIR__ . '/common.php';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $user = trim($_POST['user'] ?? '');
    $pass = $_POST['pass'] ?? '';

    if ($user === '' || $pass === '') {
        echo "<div style='font-family:sans-serif;text-align:center;margin-top:100px;'>
                ユーザー名とパスワードを入力してください。<br>
                <a href='register.php'>戻る</a>
              </div>";
        exit;
    }

    $pdo = get_pdo();

    // 既存ユーザー確認
    $stmt = $pdo->prepare("SELECT id FROM users WHERE username = :u LIMIT 1");
    $stmt->execute([':u' => $user]);
    if ($stmt->fetch(PDO::FETCH_ASSOC)) {
        echo "<div style='font-family:sans-serif;text-align:center;margin-top:100px;'>
                このユーザーIDは既に存在します。<br>
                <a href='register.php'>戻る</a>
              </div>";
        exit;
    }

    // ユーザー作成
    $hash = password_hash($pass, PASSWORD_DEFAULT);
    $icon = 'img/default.jpg';
    $role = 'user';

    $stmt = $pdo->prepare("
        INSERT INTO users (username, password_hash, icon, role)
        VALUES (:u, :p, :i, :r)
    ");
    $stmt->execute([
        ':u' => $user,
        ':p' => $hash,
        ':i' => $icon,
        ':r' => $role,
    ]);

    write_log("USER REGISTERED user={$user}");

    echo "<div style='font-family:sans-serif;text-align:center;margin-top:100px;'>
            アカウントを作成しました。<br>
            <a href='login.php'>ログイン画面へ</a>
          </div>";
    exit;
}
?>
<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <title>アカウント作成</title>
  <link rel="stylesheet" href="css/reset.css">
  <link rel="stylesheet" href="css/style.css">
  <link rel="icon" href="img/logo.png">
  <style>
  </style>
</head>
<body id="register">
  <div class="card">
    <img class="logo" src="img/YUKA_logo_remove_review.png" alt="">
    <h1>Umegle アカウントを作成</h1>
    <p>1つのアカウントですべてのUmegleサービスを利用できます</p>
    <form method="post">
      <label for="user">ユーザーID</label>
      <input type="text" id="user" name="user" required>

      <label for="pass">パスワード</label>
      <input type="password" id="pass" name="pass" required>

      <input type="submit" value="作成">
    </form>
    <div class="yet">
      <a href="login.php">既にアカウントをお持ちですか？</a>
    </div>
    <footer>
      © 2025 Umegle
    </footer>
  </div>
</body>
</html>
