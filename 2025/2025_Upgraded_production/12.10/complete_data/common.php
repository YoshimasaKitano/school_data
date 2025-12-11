<?php
require_once __DIR__ . '/db.php';

// DB とセッションの初期化
init_database();
init_session();

/**
 * ログ記録（時刻・IP・内容を DB に保存）
 */
function write_log($message) {
    try {
        $pdo  = get_pdo();
        $user = isset($_SESSION['user']) ? $_SESSION['user'] : null;
        $ip   = isset($_SERVER['REMOTE_ADDR']) ? $_SERVER['REMOTE_ADDR'] : 'unknown';
        $stmt = $pdo->prepare("
            INSERT INTO logs (user, ip, message)
            VALUES (:user, :ip, :message)
        ");
        $stmt->execute([
            ':user'    => $user,
            ':ip'      => $ip,
            ':message' => $message,
        ]);
    } catch (Throwable $e) {
        // ログ書き込みが失敗してもアプリ本体は止めない
        error_log('write_log failed: ' . $e->getMessage());
    }
}

/**
 * ログイン状態を確認
 * 未ログインなら login.php へ強制リダイレクト
 */
function check_login() {
    if (empty($_SESSION['user'])) {
        header('Location: login.php');
        exit;
    }
}
?>
