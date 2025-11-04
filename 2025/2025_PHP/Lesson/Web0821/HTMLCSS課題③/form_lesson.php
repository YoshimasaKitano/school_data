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
                <p class="formtext"><label>お名前：(必須)<input type="text" name="name" placeholder=" お名前" required class="formbox"></label></p>
                <p class="formtext"><label>メールアドレス：(必須)<input type="email" name="email" placeholder=" example.123@example.cor" required class="formbox"></label></p>
                <p class="formtext"><label>電話番号：<input type="tel" name="tel" placeholder=" 00000000000" class="formbox"></label></p>
                <p class="formtext">
                    <label>性別：</label>
                    <label><input type="radio" name="gender" value="男性" checked="checked" class="gendertext">男性</label>
                    <label><input type="radio" name="gender" value="女性" class="gendertext">女性</label>
                    <label><input type="radio" name="gender" value="その他" class="gendertext">その他</label>
                </p>
                <p class="formtext">
                    <label>一番好きな動物は？：</label>
                    <select name="animal" class="formbox">
                        <option value="" selected hidden>選択してください</option>
                        <option value="horse">ウマ</option>
                        <option value="hippopotamus">カバ</option>
                        <option value="capybara">カピバラ</option>
                        <option value="giraffe">キリン</option>
                        <option value="peacock">クジャク</option>
                        <option value="koala">コアラ</option>
                        <option value="bat">コウモリ</option>
                        <option value="gorilla">ゴリラ</option>
                        <option value="monkey">サル</option>
                        <option value="zebra">シマウマ</option>
                        <option value="elephant">ゾウ</option>
                        <option value="panda">パンダ</option>
                        <option value="sheep">ヒツジ</option>
                        <option value="flamingo">フラミンゴ</option>
                        <option value="lion">ライオン</option>
                        <option value="giraffe">キリン</option>
                        <option value="others_animal">その他</option>
                    </select>
                </p>
                <p class="formtext">
                    <label>OCAサファリパークはいかがでしたか？ご意見・ご感想をお願いします！</label>
                    <textarea name="comment" cols="120" rows="12" placeholder="コメントを入力してください"></textarea>
                </p>
                <p class="formtext"><label><input type="checkbox" value="personal" required>個人情報保護法に同意します。(必須)</label></p>
                <p class="formtext"><a href="personal_information.html" target="_blank" class="formpersonal">個人情報のお取扱いについて</p>
                <ul>
                    <li><input type="reset" value="リセット"></li>
                    <li><input type="submit" value="送信"></li>
                </ul>
            </form>
        </div>
    </main>
    <?php include(dirname(__FILE__) .'/files/footer.html'); ?>
    <script src="js/main.js"></script>
</body>
</html>