<?php
    session_start();

    $flash = empty($_SESSION['flash']) ? [] : $_SESSION['flash'];
    unset($_SESSION['flash']);

    $original = empty($_SESSION['original']) ? [] : $_SESSION['original'];
    unset($_SESSION['original']);

    // トークン生成
    $toke_byte = random_bytes(16);
    $token = bin2hex($toke_byte);

    $_SESSION['token'] = $token;
?>
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>OCAサファリパーク in OSAKA</title>
    <link rel="stylesheet" href="css/reset.css">
    <link rel="stylesheet" href="css/style.css">
    <link rel="shortcut icon" href="images/logo50.png">
    <script src="https://kit.fontawesome.com/6643e64c88.js" crossorigin="anonymous"></script>
    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.8.3/jquery.min.js"></script>
</head>
<body>
    <?php include(dirname(__FILE__) .'/files/header.html'); ?>
    <main>
        <h2>ご来場者プレゼント</h2>
        <div class="formpage">
            <h3>本日はご来場いただきありがとうございました。感謝の気持ちを込めて、アニマルグッズをプレゼントいたします。以下のフォームよりご応募ください。</h3>
            <form action="confirm.php" method="POST">
                <!-- <p><label for="name">名前</label><input type="text" name="name" id="name"></p> -->
                <p class="formtext"><label>お名前：(必須)<input type="text" name="name" value = "<?=empty($original['name']) ? null : $original['name'];?>" placeholder=" お名前" class="formbox"></label><?=empty($flash['name']) ? null : $flash['name'];?></p>
                <p class="formtext"><label>メールアドレス：(必須)<input type="email" name="email" value = "<?=empty($original['email']) ? null : $original['email'];?>" placeholder=" example.123@example.cor" class="formbox"></label><?=empty($flash['email']) ? null : $flash['email'];?></p>
                <p class="formtext"><label>電話番号：(必須)<input type="tel" name="tel" value="<?=empty($original['tel']) ? null : $original['tel'];?>" placeholder=" 00000000000" class="formbox"></label><?=empty($flash['tel']) ? null : $flash['tel'];?></p>
                <p class="formtext">
                    <label>性別：(必須)</label>
                    <label><input type="radio" name="gender" value="男性" class="gendertext" <?php if (!empty($original['gender']))  {if ("男性" === $original['gender'])  {echo 'checked';} } ?>>男性</label>
                    <label><input type="radio" name="gender" value="女性" class="gendertext" <?php if (!empty($original['gender'])) {if ("女性" === $original['gender'])  {echo 'checked';} } ?>>女性</label>
                    <label><input type="radio" name="gender" value="その他" class="gendertext" <?php if (!empty($original['gender'])) {if ("その他" === $original['gender']) {echo 'checked';} } ?>>その他</label>
                    <?=empty($flash['gender']) ? null : $flash['gender'];?>
                </p>
                <p class="formtext">
                    <label>一番好きな動物は？：(必須)</label>
                    <select name="animal" class="formbox">
                        <option value="" selected hidden>選択してください</option>
                        <option value="ウマ" <?php if (!empty($original['animal'])) {if ("ウマ" === $original['animal']) { echo 'selected';} } ?>>ウマ</option>
                        <option value="カバ" <?php if (!empty($original['animal'])) {if ("カバ" === $original['animal']) { echo 'selected';} } ?>>カバ</option>
                        <option value="カピバラ" <?php if (!empty($original['animal'])) {if ("カピバラ" === $original['animal']) { echo 'selected';} } ?>>カピバラ</option>
                        <option value="キリン" <?php if (!empty($original['animal'])) {if ("キリン" === $original['animal']) { echo 'selected';} } ?>>キリン</option>
                        <option value="クジャク" <?php if (!empty($original['animal'])) {if ("クジャク" === $original['animal']) { echo 'selected';} } ?>>クジャク</option>
                        <option value="コアラ" <?php if (!empty($original['animal'])) {if ("コアラ" === $original['animal']) { echo 'selected';} } ?>>コアラ</option>
                        <option value="コウモリ" <?php if (!empty($original['animal'])) {if ("コウモリ" === $original['animal']) { echo 'selected';} } ?>>コウモリ</option>
                        <option value="ゴリラ" <?php if (!empty($original['animal'])) {if ("ゴリラ" === $original['animal']) { echo 'selected';} } ?>>ゴリラ</option>
                        <option value="サル" <?php if (!empty($original['animal'])) {if ("サル" === $original['animal']) { echo 'selected';} } ?>>サル</option>
                        <option value="シマウマ" <?php if (!empty($original['animal'])) {if ("シマウマ" === $original['animal']) { echo 'selected';} } ?>>シマウマ</option>
                        <option value="ゾウ" <?php if (!empty($original['animal'])) {if ("ゾウ" === $original['animal']) { echo 'selected';} } ?>>ゾウ</option>
                        <option value="パンダ" <?php if (!empty($original['animal'])) {if ("パンダ" === $original['animal']) { echo 'selected';} } ?>>パンダ</option>
                        <option value="ヒツジ" <?php if (!empty($original['animal'])) {if ("ヒツジ" === $original['animal']) { echo 'selected';} } ?>>ヒツジ</option>
                        <option value="フラミンゴ" <?php if (!empty($original['animal'])) {if ("フラミンゴ" === $original['animal']) { echo 'selected';} } ?>>フラミンゴ</option>
                        <option value="ライオン" <?php if (!empty($original['animal'])) {if ("ライオン" === $original['animal']) { echo 'selected';} } ?>>ライオン</option>
                        <option value="ワニ" <?php if (!empty($original['animal'])) {if ("ワニ" === $original['animal']) { echo 'selected';} } ?>>ワニ</option>
                        <option value="その他" <?php if (!empty($original['animal'])) {if ("その他" === $original['animal']) { echo 'selected';} } ?>>その他</option>
                    </select>
                    <?=empty($flash['animal']) ? null : $flash['animal'];?>
                </p>
                <p class="formtext">
                    <label>OCAサファリパークはいかがでしたか？ご意見・ご感想をお願いします！(必須)</label><?=empty($flash['comment']) ? null : $flash['comment'];?>
                    <textarea name="comment" cols="120" rows="12" placeholder="コメントを入力してください"><?=empty($original['comment']) ? null : $original['comment'];?></textarea>
                </p>
                <p class="formtext"><label><input type="checkbox" name="agree" value="1" <?php if (!empty($original['agree'])) {echo 'checked';} ?>>個人情報保護法に同意します。(必須)<?=empty($flash['agree']) ? null : $flash['agree'];?></label></p>
                <p class="formtext"><a href="personal_information.html" target="_blank" class="formpersonal">個人情報のお取扱いについて</p>
            <!-- トークンの送信 -->
                <input type="hidden" name="token" value="<?php echo $token;?>">
                <ul>
                    <li><input type="reset" name="リセット"></li>
                    <li><input type="submit" name="submit" value="送信"></li>
                </ul>
            </form>
        </div>
    </main>
    <?php include(dirname(__FILE__) .'/files/footer.html'); ?>
    <script src="js/main.js"></script>
</body>
</html>