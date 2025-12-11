<?php
require_once __DIR__ . '/common.php';

$user = $_POST['user'] ?? '';
$pass = $_POST['pass'] ?? '';

// ログイン失敗回数制限
if (!isset($_SESSION['fail_count'])) {
    $_SESSION['fail_count'] = 0;
}

$pdo = get_pdo();
$stmt = $pdo->prepare("SELECT id, username, password_hash, icon, role FROM users WHERE username = :u LIMIT 1");
$stmt->execute([':u' => $user]);
$row = $stmt->fetch(PDO::FETCH_ASSOC);

if ($row) {
    $stored = $row['password_hash'];

    // 両対応チェック：password_verify（ハッシュ）または平文一致
    $isValid = password_verify($pass, $stored) || $pass === $stored;

    if ($isValid) {
        // ログイン成功
        $_SESSION['user_id'] = (int)$row['id'];
        $_SESSION['user']    = $row['username'];
        $_SESSION['icon']    = $row['icon'] ?: 'img/default.jpg';
        $_SESSION['role']    = $row['role'] ?: 'user';
        $_SESSION['fail_count'] = 0;

        write_log("LOGIN SUCCESS user={$row['username']}");

        header('Location: chat.php');
        exit;
    }
}

// ログイン失敗処理
$_SESSION['fail_count']++;
write_log("LOGIN FAILED user=$user");

// ログイン失敗回数が多い場合のメッセージ
if ($_SESSION['fail_count'] >= 3) {
    echo "ログイン失敗が3回続きました。<br>しばらく後にお試しください。";
    exit;
}

echo "ログイン失敗。<a href='login.php'>戻る</a>";
?>
