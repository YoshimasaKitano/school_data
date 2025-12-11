<?php
// db.php
// MySQL 接続 + セッションハンドラ + 共通 DB ヘルパー

// =========================================
// DB 接続設定（環境に合わせて変更）
// =========================================

// define('DB_DSN', 'mysql:host=ホスト名;dbname=データベース名;charset=utf8mb4');
if (!defined('DB_DSN')) {
    define('DB_DSN', 'mysql:host=localhost;dbname=oca;charset=utf8mb4');
}

// define('DB_USER', 'MySQL ユーザー名');
if (!defined('DB_USER')) {
    define('DB_USER', 'root');
}

// define('DB_PASS', 'パスワード');
if (!defined('DB_PASS')) {
    define('DB_PASS', 'Pa$$w0rd');
}

/**
 * 共通 PDO インスタンス取得
 */
function get_pdo() {
    static $pdo = null;
    if ($pdo instanceof PDO) {
        return $pdo;
    }
    try {
        $pdo = new PDO(DB_DSN, DB_USER, DB_PASS, [
            PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
            PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
        ]);
    } catch (Throwable $e) {
        error_log('DB connection failed: ' . $e->getMessage());
        die('データベース接続エラー');
    }
    return $pdo;
}

/**
 * アプリで利用するテーブルを作成
 * （存在しない場合のみ）
 */
function init_database() {
    $pdo = get_pdo();

    // users テーブル
    $pdo->exec("
        CREATE TABLE IF NOT EXISTS users (
            id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(191) NOT NULL UNIQUE,
            password_hash VARCHAR(255) NOT NULL,
            icon VARCHAR(255) DEFAULT 'img/default.jpg',
            role VARCHAR(50) DEFAULT 'user',
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
    ");


    // ユーザーごとのパーソナライズ設定
    $pdo->exec("
        CREATE TABLE IF NOT EXISTS user_settings (
            user_id INT UNSIGNED PRIMARY KEY,
            user_profile TEXT,
            assistant_style TEXT,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            CONSTRAINT fk_user_settings_user FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
    ");

    // ログテーブル
    $pdo->exec("
        CREATE TABLE IF NOT EXISTS logs (
            id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
            user VARCHAR(191) NULL,
            ip VARCHAR(45) NULL,
            message TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            INDEX idx_logs_user (user),
            INDEX idx_logs_created_at (created_at)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
    ");

    // チャットルーム
    $pdo->exec("
        CREATE TABLE IF NOT EXISTS chat_rooms (
            id VARCHAR(191) PRIMARY KEY,
            name VARCHAR(255),
            archived TINYINT(1) DEFAULT 0,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
    ");

    // 会話ログ
    $pdo->exec("
        CREATE TABLE IF NOT EXISTS ai_conversations (
            id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
            room_id VARCHAR(191),
            user_id VARCHAR(191),
            role VARCHAR(50),
            message TEXT,
            meta_json TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            INDEX idx_ai_conv_room (room_id),
            INDEX idx_ai_conv_user (user_id),
            INDEX idx_ai_conv_created (created_at)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
    ");

    // セッションテーブル
    $pdo->exec("
        CREATE TABLE IF NOT EXISTS app_sessions (
            id VARCHAR(128) PRIMARY KEY,
            data BLOB,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            last_updated DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
    ");
}

// =========================================
// セッションハンドラ（DB 保存）
// =========================================
class DbSessionHandler implements SessionHandlerInterface
{
    private $pdo;
    private $table;

    public function __construct(PDO $pdo, $table = 'app_sessions') {
        $this->pdo   = $pdo;
        $this->table = $table;
    }

    public function open($save_path, $session_name) {
        return true;
    }

    public function close() {
        return true;
    }

    public function read($id) {
        try {
            $stmt = $this->pdo->prepare("SELECT data FROM {$this->table} WHERE id = :id");
            $stmt->execute([':id' => $id]);
            if ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
                return (string)$row['data'];
            }
        } catch (Throwable $e) {
            error_log('Session read error: ' . $e->getMessage());
        }
        return '';
    }

    public function write($id, $data) {
        try {
            $stmt = $this->pdo->prepare("
                INSERT INTO {$this->table} (id, data, created_at, last_updated)
                VALUES (:id, :data, NOW(), NOW())
                ON DUPLICATE KEY UPDATE data = VALUES(data), last_updated = NOW()
            ");
            return $stmt->execute([
                ':id'   => $id,
                ':data' => $data,
            ]);
        } catch (Throwable $e) {
            error_log('Session write error: ' . $e->getMessage());
            return false;
        }
    }

    public function destroy($id) {
        try {
            $stmt = $this->pdo->prepare("DELETE FROM {$this->table} WHERE id = :id");
            return $stmt->execute([':id' => $id]);
        } catch (Throwable $e) {
            error_log('Session destroy error: ' . $e->getMessage());
            return false;
        }
    }

    public function gc($maxlifetime) {
        try {
            $stmt = $this->pdo->prepare("
                DELETE FROM {$this->table}
                WHERE last_updated < DATE_SUB(NOW(), INTERVAL :sec SECOND)
            ");
            $stmt->bindValue(':sec', (int)$maxlifetime, PDO::PARAM_INT);
            return $stmt->execute();
        } catch (Throwable $e) {
            error_log('Session gc error: ' . $e->getMessage());
            return false;
        }
    }
}

/**
 * セッション初期化（DB バックエンド）
 */
function init_session() {
    // すでに開始済みなら何もしない
    if (session_status() !== PHP_SESSION_NONE) {
        return;
    }
    $pdo = get_pdo();
    // 念のためテーブル作成
    $pdo->exec("
        CREATE TABLE IF NOT EXISTS app_sessions (
            id VARCHAR(128) PRIMARY KEY,
            data BLOB,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            last_updated DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
    ");
    $handler = new DbSessionHandler($pdo, 'app_sessions');
    session_set_save_handler($handler, true);
    session_start();
}
