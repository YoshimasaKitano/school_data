<?php require 'common.php'; ?>
<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <title>ログイン - Umegle</title>
  <link rel="stylesheet" href="css/reset.css">
  <link rel="stylesheet" href="css/style.css">
  <link rel="icon" href="img/logo.png">
<!-- スマートフォンなどのモバイルデバイスで適切に表示されるようにするためのHTMLメタタグ -->
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body id="login">
  <div class="login-card">
    <img src="img\logo.png" alt="Umegle" class="logo">
    <h1>ログイン</h1>
    <p class="sub">お使いの Umegle アカウントにアクセス</p>

    <form method="post" action="auth.php">
      <label for="user">ユーザーID</label>
      <input type="text" id="user" name="user" required>

      <label for="pass">パスワード</label>
      <input type="password" id="pass" name="pass" required>

      <input type="submit" value="ログイン">
    </form>

    <div class="register">
      <p><a href="register.php">アカウントを作成</a></p>
    </div>

    <footer>
      © 2025 Umegle
    </footer>
  </div>
</body>
</html>
