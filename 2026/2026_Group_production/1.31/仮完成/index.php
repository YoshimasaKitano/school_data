<?php
require 'common.php';
check_login();
$user = $_SESSION['user'];
$icon = $_SESSION['icon'];
$role = $_SESSION['role'];
?>
<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>__進級課題__</title>
  <link rel="stylesheet" href="css/reset.css">
  <link rel="stylesheet" href="css/style.css">
  <link rel="icon" href="img/logo.png">
</head>
<body id="index">
  <header>
    <ul class="menu">
      <!-- <li>maile</li> -->
      <li><a href="#"><img src="" alt=""></a></li>
      <nav class="user_menu" aria-label="ユーザーメニュー">
        <input type="checkbox" id="toggleMenu">
        <label for="toggleMenu" class="user-icon-btn">
          <img src="<?= htmlspecialchars($icon) ?>" alt="アイコン">
        </label>

        <div class="dropdown-content" id="userDropdown">
          <div class="dropdown-header">
            <img src="<?= htmlspecialchars($icon) ?>" alt="アイコン">
            <div>
              <div class="username"><?= htmlspecialchars($user) ?></div>
              <?php if ($role === 'admin'): ?>
                <div style="font-size: 12px; color: #777;">管理者</div>
              <?php else: ?>
                <div style="font-size: 12px; color: #777;">一般ユーザー</div>
              <?php endif; ?>
            </div>
          </div>

          <a href="upload_icon.php" class="dropdown-link">プロフィール画像を変更</a>
          <?php if ($role === 'admin'): ?>
            <a href="admin.php" class="dropdown-link" style="color:#1a73e8;">管理者画面</a>
          <?php endif; ?>

          <!-- <div class="account-list">
            <div class="account-item">
              <img src="img/ume.jpeg" alt="ume">
              <span>ume（管理者）</span>
            </div>
            <div class="account-item">
              <img src="img/host.jpg" alt="host">
              <span>host（一般ユーザー）</span>
            </div>
          </div> -->

          <a href="logout.php" class="dropdown-link logout">ログアウト</a>
        </div>
        <div class="overlay"></div>
      </nav>
    </ul>
  </header>

  <main>
    <h1 class="title"><img src="img\logo.png" alt="Umegle" class="google-logo"></h1>

    <form method="get" id="form" action="chat.php">
      <button id="sbtn" type="submit"><img src="img/serch_icon.png" alt="Button Image" class="serch_icon"></button>
      <input id="sbox" name="s" type="text" placeholder="キーワードを入力">
    </form>

    <ul class="rink">
      <li>
        <a href="#">
          <img src="img\cut_icon.png" alt="icon1">
          <p>校内wiki</p>
        </a>
      </li>
      <li>
        <a href="chat.php">
          <img src="img\cut_icon.png" alt="icon2">
          <p>Chatoor</p>
        </a>
      </li>
    </ul>

  </main>

  <footer></footer>
</body>
</html>
