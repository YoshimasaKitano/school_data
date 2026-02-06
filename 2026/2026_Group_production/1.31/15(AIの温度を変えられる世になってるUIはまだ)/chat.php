<?php
// ==============================================
//  ChatOCA - MySQL 対応版
// ==============================================
require_once __DIR__ . '/common.php';

check_login();

$server_user = trim($_SESSION['user']);
$server_icon = isset($_SESSION['icon']) ? trim($_SESSION['icon']) : 'img/default.jpg';

/**
 * HTML エスケープ
 */
function h($s)
{
    return htmlspecialchars($s, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8');
}

define('MAX_MESSAGE_LENGTH', 2000);
define('MAX_ROOM_NAME_LENGTH', 100);

// ==============================================
// AI バックエンド呼び出し関数（Python create_AI）
// ==============================================
/**
 * @param string $question
 * @return string
 */
function call_ai_backend($question)
{
    // Python スクリプトのパス
    $script = __DIR__ . '/create_AI/ai_bridge.py';

    if (!file_exists($script)) {
        error_log('AI script not found: ' . $script);
        return 'AIスクリプトが見つかりませんでした。';
    }

    $descriptorspec = [
        0 => ['pipe', 'r'],  // stdin
        1 => ['pipe', 'w'],  // stdout
        2 => ['pipe', 'w'],  // stderr
    ];

    // create_AI ディレクトリをカレントディレクトリにして実行
    $cwd = __DIR__ . '/create_AI';

    // OS に応じて Python コマンド名を決定（Windows: python, Unix 系: python3）
    $python = (stripos(PHP_OS_FAMILY, 'Windows') !== false) ? 'python' : 'python3';
    $cmd    = escapeshellcmd($python) . ' ' . escapeshellarg($script);

    $process = @proc_open($cmd, $descriptorspec, $pipes, $cwd);

    if (!is_resource($process)) {
        error_log('failed to start AI process');
        return 'AIプロセスを起動できませんでした。';
    }

    // 質問を JSON で Python 側に渡す
        // 現在ログイン中ユーザーのパーソナライズ設定を取得
    $user_profile = '';
    $assistant_style = '';
    try {
        if (isset($_SESSION['user_id'])) {
            $pdo_for_ai = get_pdo();
            $pdo_for_ai->exec("
                CREATE TABLE IF NOT EXISTS user_settings (
                    user_id INT UNSIGNED PRIMARY KEY,
                    user_profile TEXT,
                    assistant_style TEXT,
                    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
            ");
            $stmt = $pdo_for_ai->prepare("SELECT user_profile, assistant_style FROM user_settings WHERE user_id = :uid LIMIT 1");
            $stmt->execute([':uid' => (int)$_SESSION['user_id']]);
            if ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
                $user_profile = (string)($row['user_profile'] ?? '');
                $assistant_style = (string)($row['assistant_style'] ?? '');
            }
        }
    } catch (Throwable $e) {
        error_log('load user_settings error: ' . $e->getMessage());
    }

    // 質問 + パーソナライズ情報を JSON で Python 側に渡す
    $payload_array = ['question' => $question];
    if ($user_profile !== '' || $assistant_style !== '') {
        $payload_array['user_profile'] = $user_profile;
        $payload_array['assistant_style'] = $assistant_style;
    }
    $payload = json_encode(
        $payload_array,
        JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES
    );

    fwrite($pipes[0], $payload);
    fclose($pipes[0]);

    $stdout = stream_get_contents($pipes[1]);
    fclose($pipes[1]);

    $stderr = stream_get_contents($pipes[2]);
    fclose($pipes[2]);

    $return_value = proc_close($process);

    // プロセスの終了コードが 0 以外ならエラー扱い
    if ($return_value !== 0) {
        error_log('AI process exit code: ' . $return_value . ' stderr: ' . $stderr);
        return 'AI連携でエラーが発生しました。';
    }

    $stdout = trim($stdout);
    if ($stdout === '') {
        return 'AIから応答がありませんでした。';
    }

    // Python 側からの JSON を解釈
    $data = json_decode($stdout, true);

    if (is_array($data)) {
        if (isset($data['answer']) && is_string($data['answer']) && $data['answer'] !== '') {
            return $data['answer'];
        }

        if (!empty($data['error']) && is_string($data['error'])) {
            error_log('AI backend error: ' . $data['error']);
            return 'AI内部でエラーが発生しました。';
        }
    }

    // JSON でない場合は生の文字列として返す
    return $stdout;
}


$pdo = get_pdo();

// ==============================================
// AJAX アクション処理
// ==============================================
if (php_sapi_name() !== 'cli' && isset($_POST['__action'])) {
    header('Content-Type: application/json; charset=utf-8');
    $action = $_POST['__action'];

    // 必要なテーブルがなければ作成
    $pdo->exec("
        CREATE TABLE IF NOT EXISTS chat_rooms (
            id VARCHAR(191) PRIMARY KEY,
            name VARCHAR(255),
            archived TINYINT(1) DEFAULT 0,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
    ");
    $pdo->exec("
        CREATE TABLE IF NOT EXISTS ai_conversations (
            id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
            room_id VARCHAR(191),
            user_id VARCHAR(191),
            role VARCHAR(50),
            message TEXT,
            meta_json TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
    ");

    try {
        switch ($action) {
            case 'rename_room':
                $room_id  = $_POST['room_id'] ?? '';
                $new_name = trim($_POST['new_name'] ?? '');
                if ($room_id === '' || $new_name === '') {
                    echo json_encode(['ok' => false, 'error' => '名前は空にできません']);
                    break;
                }
                if (mb_strlen($new_name) > MAX_ROOM_NAME_LENGTH) {
                    echo json_encode(['ok' => false, 'error' => '名前が長すぎます']);
                    break;
                }
                $stmt = $pdo->prepare("
                    INSERT INTO chat_rooms (id, name, archived)
                    VALUES (:id, :name, 0)
                    ON DUPLICATE KEY UPDATE name = VALUES(name)
                ");
                $stmt->execute([':id' => $room_id, ':name' => $new_name]);
                echo json_encode(['ok' => true]);
                break;

            case 'delete_room':
                $room_id = $_POST['room_id'] ?? '';
                if ($room_id === '') {
                    echo json_encode(['ok' => false, 'error' => 'room_id が不正です']);
                    break;
                }
                $stmt = $pdo->prepare("DELETE FROM chat_rooms WHERE id = :id");
                $stmt->execute([':id' => $room_id]);
                $stmt = $pdo->prepare("DELETE FROM ai_conversations WHERE room_id = :id");
                $stmt->execute([':id' => $room_id]);
                echo json_encode(['ok' => true]);
                break;

            case 'create_room':
                $name = trim($_POST['name'] ?? '');
                if ($name === '') {
                    echo json_encode(['ok' => false, 'error' => '名前は空にできません']);
                    break;
                }
                if (mb_strlen($name) > MAX_ROOM_NAME_LENGTH) {
                    echo json_encode(['ok' => false, 'error' => '名前が長すぎます']);
                    break;
                }
                // シンプルな ID 生成
                $id = 'room_' . bin2hex(random_bytes(8));
                $stmt = $pdo->prepare("INSERT INTO chat_rooms (id, name, archived) VALUES (:id, :name, 0)");
                $stmt->execute([':id' => $id, ':name' => $name]);
                echo json_encode(['ok' => true, 'id' => $id, 'name' => $name]);
                break;

            case 'set_archive':
                $room_id = $_POST['room_id'] ?? '';
                $archive = intval($_POST['archive'] ?? 1);
                if ($room_id === '') {
                    echo json_encode(['ok' => false, 'error' => 'room_id が不正です']);
                    break;
                }
                $stmt = $pdo->prepare("
                    INSERT INTO chat_rooms (id, name, archived)
                    VALUES (:id, :id, :archived)
                    ON DUPLICATE KEY UPDATE archived = VALUES(archived)
                ");
                $stmt->execute([
                    ':id'       => $room_id,
                    ':archived' => $archive,
                ]);
                echo json_encode(['ok' => true]);
                break;

            default:
                echo json_encode(['ok' => false, 'error' => '不明なアクション']);
        }
    } catch (Throwable $e) {
        error_log('chat.php ajax error: ' . $e->getMessage());
        echo json_encode(['ok' => false, 'error' => 'サーバーエラー']);
    }
    exit;
}

// ==============================================
// 通常のチャット処理
// ==============================================
$mode = $_GET['mode'] ?? 'chat';
$initial_mode = $mode;
$room = trim($_GET['room'] ?? 'general');

if (!isset($_SESSION['room'])) {
    $_SESSION['room'] = [];
}
if (!isset($_SESSION['room'][$room])) {
    $_SESSION['room'][$room] = [];
}

// 変更後：chat モードでは「新しいチャット」を作成し、room モードでは選択済みルームで続きの会話を行う
if ($_SERVER['REQUEST_METHOD'] === 'POST' && in_array($mode, ['chat', 'room'], true)) {
    $user_msg = trim($_POST['message'] ?? '');
    if ($user_msg !== '') {
        if (mb_strlen($user_msg) > MAX_MESSAGE_LENGTH) {
            $user_msg = mb_substr($user_msg, 0, MAX_MESSAGE_LENGTH);
        }

        // chat モードからの投稿なら、新しいルームを発行してそちらに紐づける
        if ($mode === 'chat') {
            // シンプルな ID 生成（既存の AJAX create_room と同じルール）
            $new_room_id = 'room_' . bin2hex(random_bytes(8));

            // ルーム名は最初のメッセージから先頭 MAX_ROOM_NAME_LENGTH 文字を利用
            $base = preg_replace('/\s+/', ' ', $user_msg);
            $base = trim($base);
            if ($base === '') {
                $base = '新しいチャット';
            }
            $room_name = mb_substr($base, 0, MAX_ROOM_NAME_LENGTH);

            try {
                $pdo->exec("
                    CREATE TABLE IF NOT EXISTS chat_rooms (
                        id VARCHAR(191) PRIMARY KEY,
                        name VARCHAR(255),
                        archived TINYINT(1) DEFAULT 0,
                        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
                    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
                ");
                $stmt = $pdo->prepare("INSERT INTO chat_rooms (id, name, archived) VALUES (:id, :name, 0)");
                $stmt->execute([':id' => $new_room_id, ':name' => $room_name]);
            } catch (Throwable $e) {
                error_log('chat.php create room on chat-post error: ' . $e->getMessage());
            }

            // 新しいルームで会話を開始する
            $room = $new_room_id;
            $mode = 'room';
        }

        $ai_reply = call_ai_backend($user_msg);

        // セッション上にも保持（既存の UI を壊さない）
        if (!isset($_SESSION['room'][$room])) {
            $_SESSION['room'][$room] = [];
        }
        $_SESSION['room'][$room][] = ['role' => 'user', 'text' => $user_msg];
        $_SESSION['room'][$room][] = ['role' => 'ai',   'text' => $ai_reply];

        // DB にも保存
        try {
            $pdo->exec("
                CREATE TABLE IF NOT EXISTS ai_conversations (
                    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
                    room_id VARCHAR(191),
                    user_id VARCHAR(191),
                    role VARCHAR(50),
                    message TEXT,
                    meta_json TEXT,
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
            ");
            $stmt = $pdo->prepare("
                INSERT INTO ai_conversations (room_id, user_id, role, message, meta_json)
                VALUES (:room, :user, :role, :msg, :meta)
            ");
            // user 発言
            $stmt->execute([
                ':room' => $room,
                ':user' => $server_user,
                ':role' => 'user',
                ':msg'  => $user_msg,
                ':meta' => json_encode(['icon' => $server_icon], JSON_UNESCAPED_UNICODE),
            ]);
            // AI 発言
            $stmt->execute([
                ':room' => $room,
                ':user' => 'ai',
                ':role' => 'assistant',
                ':msg'  => $ai_reply,
                ':meta' => json_encode([], JSON_UNESCAPED_UNICODE),
            ]);
        } catch (Throwable $e) {
            error_log('chat.php insert conversation error: ' . $e->getMessage());
        }

        // chat モードから来た場合は、新しいルーム画面にリダイレクト
        if ($initial_mode === 'chat') {
            header('Location: ?mode=room&room=' . urlencode($room));
            exit;
        }
    }
}

// ==============================================
// ==============================================
// パーソナライズ設定のロードと保存
// ==============================================
$user_profile     = '';
$assistant_style  = '';
$settings_saved   = false;

if (isset($_SESSION['user_id'])) {
    try {
        $pdo->exec("
            CREATE TABLE IF NOT EXISTS user_settings (
                user_id INT UNSIGNED PRIMARY KEY,
                user_profile TEXT,
                assistant_style TEXT,
                updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
        ");
        $stmt = $pdo->prepare("SELECT user_profile, assistant_style FROM user_settings WHERE user_id = :uid LIMIT 1");
        $stmt->execute([':uid' => (int)$_SESSION['user_id']]);
        if ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
            $user_profile    = (string)($row['user_profile'] ?? '');
            $assistant_style = (string)($row['assistant_style'] ?? '');
        }
    } catch (Throwable $e) {
        error_log('load user_settings view error: ' . $e->getMessage());
    }
}

// 設定画面からの保存リクエスト
if ($_SERVER['REQUEST_METHOD'] === 'POST' && $mode === 'settings') {
    $profile = trim($_POST['user_profile'] ?? '');
    $style   = trim($_POST['assistant_style'] ?? '');

    try {
        $pdo->exec("
            CREATE TABLE IF NOT EXISTS user_settings (
                user_id INT UNSIGNED PRIMARY KEY,
                user_profile TEXT,
                assistant_style TEXT,
                updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
        ");
        $stmt = $pdo->prepare("
            INSERT INTO user_settings (user_id, user_profile, assistant_style)
            VALUES (:uid, :profile, :style)
            ON DUPLICATE KEY UPDATE
                user_profile = VALUES(user_profile),
                assistant_style = VALUES(assistant_style)
        ");
        $stmt->execute([
            ':uid'     => (int)($_SESSION['user_id'] ?? 0),
            ':profile' => $profile,
            ':style'   => $style,
        ]);

        $user_profile    = $profile;
        $assistant_style = $style;
        $settings_saved  = true;
    } catch (Throwable $e) {
        error_log('save user_settings error: ' . $e->getMessage());
    }
}


// DBからルーム・アーカイブ情報を取得
// ==============================================
$rooms    = [];
$archived = [];

try {
    $pdo->exec("
        CREATE TABLE IF NOT EXISTS chat_rooms (
            id VARCHAR(191) PRIMARY KEY,
            name VARCHAR(255),
            archived TINYINT(1) DEFAULT 0,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
    ");
    $stmt = $pdo->query("SELECT id, name, archived FROM chat_rooms ORDER BY created_at ASC");
    foreach ($stmt as $row) {
        if ((int)$row['archived'] === 1) {
            $archived[$row['id']] = $row['name'];
        } else {
            $rooms[$row['id']] = $row['name'];
        }
    }
} catch (Throwable $e) {
    error_log('chat.php load rooms error: ' . $e->getMessage());
}

if (empty($rooms) && empty($archived)) {
    // 初回のみ: デフォルトのルーム3つをDBに投入しておく
    try {
        $defaults = [
            'room0' => '💬 チャット1',
            'room1' => '💬 チャット2',
            'room2' => '💬 チャット3',
        ];
        $pdo->beginTransaction();
        $stmt = $pdo->prepare("INSERT IGNORE INTO chat_rooms (id, name, archived) VALUES (:id, :name, 0)");
        foreach ($defaults as $id => $name) {
            $stmt->execute([':id' => $id, ':name' => $name]);
            $rooms[$id] = $name;
        }
        $pdo->commit();
    } catch (Throwable $e) {
        if ($pdo->inTransaction()) {
            $pdo->rollBack();
        }
        error_log('chat.php seed default rooms error: ' . $e->getMessage());
        // 失敗した場合は従来どおりメモリ上だけに定義
        if (empty($rooms)) {
            $rooms = [
                'room0' => '💬 チャット1',
                'room1' => '💬 チャット2',
                'room2' => '💬 チャット3',
            ];
        }
    }
}
?>

<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ChatOCA</title>
<link rel="stylesheet" href="css/reset.css">
<link rel="stylesheet" href="css/chat_style.css">
<link rel="icon" href="img/logo.png">
</head>
<body>
<div class="sidebar">
  <div class="logo">
    <img src="img/YUKA_logo_remove_review.png" alt="logo">
  </div>
  <div class="menu">
    <a href="index.php">🏠 ホーム</a>
    <a href="?mode=chat" class="<?=($mode==='chat')?'active':''?>">💬 チャット一覧</a>
    <a href="?mode=profile" class="<?=($mode==='profile')?'active':''?>">👤 プロフィール</a>
    <a href="?mode=settings" class="<?=($mode==='settings')?'active':''?>">⚙️ 設定</a>

    <?php if(in_array($mode, ['chat','room'], true)): ?>
    <div class="room-list">
      <?php foreach($rooms as $r => $label): $active = ($r === $room)?'active':''; ?>
        <div class="room-item <?=h($active)?>" data-room-id="<?=h($r)?>">
          <span class="room-name"><?=h($label)?></span>
          <div class="mmb-menu">
            <button onclick="toggleMenu(event)">⋮</button>
            <div class="mmb-dropdown">
              <button class="room-rename-button">名前変更</button>
              <button class="room-delete-button">削除</button>
              <button class="room-archive-button">アーカイブ</button>
            </div>
          </div>
        </div>
      <?php endforeach; ?>

      <details <?= isset($archived[$room]) ? 'open' : '' ?>>
        <summary style="margin-top: 20px;">📦 アーカイブ</summary>
        <?php foreach($archived as $r => $label): ?>
        <div class="room-item" data-room-id="<?=h($r)?>">
          <span class="room-name"><?=h($label)?></span>
          <div class="mmb-menu">
            <button onclick="toggleMenu(event)">⋮</button>
            <div class="mmb-dropdown">
              <button class="room-rename-button">名前変更</button>
              <button class="room-restore-button">復元</button>
              <button class="room-delete-button">削除</button>
            </div>
          </div>
        </div>
        <?php endforeach; ?>
      </details>


      <div class="new-room">
        <input type="text" class="new-room-input" placeholder="+ 新しいルーム">
      </div>
    </div>
    <?php endif; ?>
  </div>
</div>

<div class="main">
  <div class="content">
  <?php if($mode==='profile'): ?>
    <h2>👤 プロフィール</h2>
    <div class="profile-card">
    <img src="<?=h($server_icon)?>" alt="アイコン" class="profile-icon">
    <div class="profile-info">
      <p><strong>名前:</strong> <?=h($server_user)?></p>
      <p><strong>ロール:</strong> <?=h($_SESSION['role'] ?? '未設定')?></p>
    </div>
    </div>
  <?php elseif($mode==='settings'): ?>

    <h2>⚙️ パーソナライズ設定</h2>

    <?php if(!empty($settings_saved)): ?>
      <div class="notice success">設定を保存しました。</div>
    <?php endif; ?>

    <form method="post" action="?mode=settings" class="settings-form">
      <div class="settings-group">
        <label for="user_profile">あなたについて（AIに知っておいてほしいこと）</label>
        <textarea id="user_profile" name="user_profile" rows="5" placeholder="例）OCAの〇〇専攻の学生です。将来はホワイトハッカーになりたいです。"><?=h($user_profile)?></textarea>
      </div>

      <div class="settings-group">
        <label for="assistant_style">AIの話し方・文体の希望</label>
        <textarea id="assistant_style" name="assistant_style" rows="5" placeholder="例）敬語で、丁寧だけどフレンドリーに話してほしい。回答はできるだけ簡潔に。"><?=h($assistant_style)?></textarea>
      </div>

      <div class="settings-actions">
        <button type="submit">保存する</button>
      </div>
    </form>

  <?php elseif($mode==='chat'): ?>
    <div class="new-chat-wrapper">
      <h2>💬 新しいチャット</h2>
      <p class="new-chat-hint">メッセージを入力して Enter を押すと、新しいルームで会話が開始されます。</p>
      <form method="post" action="?mode=chat" class="new-chat-form">
        <div class="new-chat-input-row">
          <input type="text" name="message" class="new-chat-input" placeholder="メッセージを入力して Enter で送信" autocomplete="off" required>
        </div>
      </form>
    </div>

<?php elseif($mode==='room'): ?>
        <div class="chat-header">ルーム: <?=h($rooms[$room] ?? $room)?></div>
      <div id="chat">
        <?php if(!empty($_SESSION['room'][$room])): ?>
          <?php foreach($_SESSION['room'][$room] as $msg): ?>
            <div class="message <?=h($msg['role'])?>">
              <?=nl2br(h($msg['text']))?>
            </div>
          <?php endforeach; ?>
        <?php else: ?>
          <p style="color:#777;text-align: center;">まだメッセージはありません。</p>
        <?php endif; ?>
      </div>
      <form method="post" class="chat-form">
        <input type="text" name="message" placeholder="メッセージを入力..." required autofocus>
        <input type="submit" value="送信">
      </form>
    <?php endif; ?>
  </div>
</div>

<script>
// =================================================
// JSユーティリティ + 各操作イベント
// =================================================
function sendAction(action, data={}) {
  data.__action = action;
  const form = new URLSearchParams(data);
  return fetch(location.href, { method:'POST', body:form }).then(r=>r.json());
}

function toggleMenu(e){
  e.stopPropagation();
  document.querySelectorAll('.mmb-dropdown').forEach(d=>d.style.display='none');
  const dd = e.target.nextElementSibling;
  if(dd) dd.style.display='block';
}
document.addEventListener('click', ()=> 
  document.querySelectorAll('.mmb-dropdown').forEach(d=>d.style.display='none')
);

// ルームクリックでチャットを開く
document.addEventListener('click', e=>{
  const room = e.target.closest('.room-item');
  if(room && !e.target.closest('.mmb-menu') && !e.target.classList.contains('room-name-input')){
    const id = room.dataset.roomId;
    
    window.location.href = `?mode=room&room=${encodeURIComponent(id)}`;
  }
});


// 名前変更
document.addEventListener('click', e=>{
  if(e.target.classList.contains('room-rename-button')){
    const room=e.target.closest('.room-item');
    const nameEl=room.querySelector('.room-name');
    const input=document.createElement('input');
    input.type='text'; input.className='room-name-input';
    input.value=nameEl.textContent.trim();
    input.dataset.roomId=room.dataset.roomId;
    nameEl.replaceWith(input);
    input.focus();
  }
});
document.addEventListener('keydown', e=>{
  const t=e.target;
  if(t.classList.contains('room-name-input') && e.key==='Enter'){
    const newName=t.value.trim(); const id=t.dataset.roomId;
    if(!newName){alert('名前は空にできません');return;}
    sendAction('rename_room',{room_id:id,new_name:newName}).then(res=>{
      if(res.ok){
        const span=document.createElement('span');
        span.className='room-name';
        span.textContent=newName;
        t.replaceWith(span);
      } else alert('変更失敗:'+res.error);
    });
  }
});

// 新規ルーム
document.addEventListener('keydown',e=>{
  const t=e.target;
  if(t.classList.contains('new-room-input') && e.key==='Enter'){
    const name=t.value.trim()||'新しいルーム';
    sendAction('create_room',{name:name}).then(r=>{
      if(r.ok){
        const div=document.createElement('div');
        div.className='room-item';
        div.dataset.roomId=r.id;
        div.innerHTML=`<span class='room-name'>${r.name}</span>
        <div class='mmb-menu'><button onclick='toggleMenu(event)'>⋮</button>
        <div class='mmb-dropdown'><button class='room-rename-button'>名前変更</button>
        <button class='room-delete-button'>削除</button>
        <button class='room-archive-button'>アーカイブ</button></div></div>`;
        document.querySelector('.room-list').insertBefore(div,document.querySelector('details'));
        t.value='';
      }
    });
  }
});

// 削除
document.addEventListener('click',e=>{
  if(e.target.classList.contains('room-delete-button')){
    const room=e.target.closest('.room-item');
    const id=room.dataset.roomId;
    if(confirm('このルームを削除しますか？')){
      sendAction('delete_room',{room_id:id}).then(r=>{
        if(r.ok) room.remove();
        else alert('削除失敗:'+r.error);
      });
    }
  }
});

// アーカイブ / 復元
document.addEventListener('click',e=>{
  if(e.target.classList.contains('room-archive-button') || e.target.classList.contains('room-restore-button')){
    const room=e.target.closest('.room-item');
    const id=room.dataset.roomId;
    const archive=e.target.classList.contains('room-archive-button')?1:0;
    sendAction('set_archive',{room_id:id,archive:archive}).then(r=>{
      if(r.ok) location.reload();
      else alert('処理失敗:'+r.error);
    });
  }
});
</script>

<!-- Auto scroll to bottom on load (added) -->
<script>
document.addEventListener('DOMContentLoaded', function () {
    try {
        var height = Math.max(
            document.body.scrollHeight || 0,
            document.documentElement.scrollHeight || 0
        );
        window.scrollTo(0, height);
    } catch (e) {
        // ignore
    }
});
</script>

</body>
</html>
