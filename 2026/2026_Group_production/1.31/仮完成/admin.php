<?php
require_once __DIR__ . '/common.php';

// 管理者チェック
check_login();
if (empty($_SESSION['role']) || $_SESSION['role'] !== 'admin') {
    http_response_code(403);
    echo "このページへアクセスする権限がありません。";
    exit;
}

$pdo = get_pdo();

// ロール変更
if (isset($_POST['change_role'])) {
    $targetUser = $_POST['username'] ?? '';
    $newRole    = $_POST['new_role'] ?? 'user';

    if ($targetUser !== '') {
        $stmt = $pdo->prepare("UPDATE users SET role = :role WHERE username = :username");
        $stmt->execute([
            ':role'     => $newRole,
            ':username' => $targetUser,
        ]);
        write_log("ROLE CHANGED user={$targetUser} role={$newRole}");
    }
}

// ユーザー削除
if (isset($_POST['delete_user'])) {
    $targetUser = $_POST['username'] ?? '';
    if ($targetUser !== '') {
        // 自分自身を削除しないようにする
        if ($targetUser === ($_SESSION['user'] ?? '')) {
            $error = '自分自身は削除できません。';
        } else {
            $stmt = $pdo->prepare("DELETE FROM users WHERE username = :username");
            $stmt->execute([':username' => $targetUser]);
            write_log("USER DELETED user={$targetUser}");
        }
    }
}

// 一覧取得
$stmt = $pdo->query("SELECT username, icon, role, created_at FROM users ORDER BY username ASC");
$users = [];
while ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
    $users[$row['username']] = [
        'icon' => $row['icon'],
        'role' => $row['role'],
        'created_at' => $row['created_at'],
    ];
}
?>
<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<title>Instagram風 管理者パネル</title>
<link rel="stylesheet" href="css/style.css">
<link rel="icon" href="img/logo.png">
</head>
<body id="admin">
<div class="navbar">
  <a href="index.php" class="nav-left">ホームに戻る</a>
  <h1>Admin</h1>
</div>

<div class="container">
  <h2>ユーザー管理</h2>
  <table>
    <tr>
      <th>ユーザー名</th>
      <th>ロール</th>
      <th>変更</th>
      <th>削除</th>
    </tr>
    <?php foreach ($users as $username => $data): ?>
    <tr>
      <td><?php echo htmlspecialchars($username); ?></td>
      <td><?php echo htmlspecialchars($data['role']); ?></td>
      <td>
        <form method="post" style="display:inline;">
          <input type="hidden" name="username" value="<?php echo htmlspecialchars($username); ?>">
          <select name="new_role">
            <option value="user" <?php if($data['role']=='user') echo 'selected'; ?>>user</option>
            <option value="admin" <?php if($data['role']=='admin') echo 'selected'; ?>>admin</option>
          </select>
          <button class="change" type="submit" name="change_role">変更</button>
        </form>
      </td>
      <td>
        <form method="post" style="display:inline;">
          <input type="hidden" name="username" value="<?php echo htmlspecialchars($username); ?>">
          <button class="delete" type="submit" name="delete_user">削除</button>
        </form>
      </td>
    </tr>
    <?php endforeach; ?>
  </table>
</div>
</body>
</html>
