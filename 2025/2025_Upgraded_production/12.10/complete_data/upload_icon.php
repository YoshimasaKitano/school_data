<?php
require_once __DIR__ . '/common.php';
check_login();

$user = $_SESSION['user'];
$pdo  = get_pdo();

if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_FILES['icon'])) {
    $file = $_FILES['icon'];

    if ($file['error'] === UPLOAD_ERR_OK) {
        $ext = strtolower(pathinfo($file['name'], PATHINFO_EXTENSION));
        if (in_array($ext, ['jpg', 'jpeg', 'png', 'gif'], true)) {
            $dir = 'img/';
            if (!is_dir($dir)) {
                mkdir($dir, 0755, true);
            }

            // ファイル名はユーザー名ベースで固定
            $filename = $dir . $user . '.' . $ext;

            if (!move_uploaded_file($file['tmp_name'], $filename)) {
                echo "ファイルの保存に失敗しました。";
                exit;
            }

            // DB 更新
            $stmt = $pdo->prepare("UPDATE users SET icon = :icon WHERE username = :username");
            $stmt->execute([
                ':icon'     => $filename,
                ':username' => $user,
            ]);

            $_SESSION['icon'] = $filename;
            write_log("ICON UPDATED user={$user} file={$filename}");

            echo "<div style='font-family:Roboto,Noto Sans JP,sans-serif;text-align:center;margin-top:100px;'>
                    <h2 style='color:#202124;'>アイコンを変更しました</h2>
                    <p><a href='index.php' style='color:#1a73e8;text-decoration:none;'>戻る</a></p>
                  </div>";
            exit;
        } else {
            echo "対応していないファイル形式です。";
            exit;
        }
    } else {
        echo "ファイルアップロード中にエラーが発生しました。";
        exit;
    }
}
?>
<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <title>プロフィール画像を変更</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="css/reset.css">
  <link rel="stylesheet" href="css/style.css">
  <link rel="icon" href="img/logo.png">
</head>
<body id="upload">
  <div class="card">
    <h1>プロフィール画像の変更</h1>
    <p class="sub">写真を更新できます</p>

    <img src="<?= htmlspecialchars($_SESSION['icon']) ?>" alt="現在のアイコン" class="icon-preview" id="preview">

    <form method="post" enctype="multipart/form-data">
      <label for="icon" class="upload-btn">画像を選択</label>
      <input type="file" name="icon" id="icon" accept="image/*" required onchange="previewImage(event)">
      <input type="submit" value="アップロード">
    </form>

    <div class="back">
      <a href="index.php">戻る</a>
    </div>
  </div>

  <script>
    // プレビュー表示
    function previewImage(event) {
      const reader = new FileReader();
      reader.onload = function() {
        const output = document.getElementById('preview');
        output.src = reader.result;
      };
      reader.readAsDataURL(event.target.files[0]);
    }
  </script>
</body>
</html>
