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