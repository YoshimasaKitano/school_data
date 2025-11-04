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
        <h2 class="animaltitle">カピバラ</h2>
        <h3 class="animalname">～テンジクネズミ科カピバラ属に分類される齧歯類～</h3>
        <div class="animalspace">
            <img src="images/84116-53-307ef32ef4fac34462aeefe7d233670d-1366x1365.webp" alt="口を開けているカピバラの写真" class="capybara">
            <p class="animal-text">体長106-134センチメートル。体重オス35-64キログラム、メス37-66キログラムと現生の齧歯類でも最大体毛はタワシのような手触りの硬く長いもので、体を震わせるだけで水を落とすことが出来る。</p>
        </div>
        <ul class="animalbtn-">
            <li class="animalbtns">
                <a href="giraffe.html" class="animalbtn"></a>
            </li>
            <li class="animal-btns">
                <a href="hippopotamus.html" class="animal-btn"></a>
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