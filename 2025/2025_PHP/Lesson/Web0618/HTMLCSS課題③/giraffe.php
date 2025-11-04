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
        <h2 class="animaltitle">キリン</h2>
        <h3 class="animalname">～哺乳綱偶蹄目キリン科キリン属に分類される偶蹄類～</h3>
        <div class="animalspace">
            <img src="images/___02.png" alt="キリンの写真" class="hipopotamus">
            <p class="animal-text">角先端までの高さオス4.7-5.3メートル、メス3.9-4.5メートル。体重オス800-1,930キログラム、メス550-1,180キログラム。体色は橙褐色や赤褐色・黒と、淡黄色からなる斑紋が入り、この斑紋は個体変異がある。</p>
        </div>
        <ul class="animalbtn-">
            <li class="animalbtns">
                <a href="peacock.html" class="animalbtn"></a>
            </li>
            <li class="animal-btns">
                <a href="capybara.html" class="animal-btn"></a>
            </li>
        </ul>
        <a href="animal.html" class="animaltop">動物たちTOPへ</a>
    </main>
    <?php include(dirname(__FILE__) .'/files/footer.html'); ?>
    <script>
        // スムーススクロール
            $(function(){
                $('a[href^=#]').click(function() {
                    var speed = 800; // scroll(ミリ秒)
                    var href = $(this).attr("href");
                    var target = $(href == "#" || href == "" ? 'html' : href);
                    var position = target.offset().top;
                    $('html').animate({scrollTop:position}, speed, 'swing');
                    return false;
                });
            });
            
            // Topへ戻るボタン
            $(function(){
                var topBtn = $('#page-top');
                //hideでボタン非表示
                topBtn.hide();
                //スクロールが1000pxに達したらボタン表示
                $(window).scroll(function(){
                    if ($(this).scrollTop() > 50){
                        topBtn.fadeIn();//もし～であれば表示
                    }else{
                        topBtn.fadeOut();//elseそうでなければ非表示
                    }
                });
                //スクロールしてトップへ戻る
                topBtn.click(function(){
                    $('body,html').animate({
                        scrollTop: 0
                    }, 500);
                    return false;
                });
            });
        </script>
</body>
</html>