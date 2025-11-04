<?php

// PHP 内部関数


// 1. 自分の名前をひらがなで変数に代入し、それをカナ変換しなさい。
// 実行結果 ヤマダタロウ


$name = 'きたのよしまさ';
echo mb_convert_kana($name, 'C');
echo '<br>';



// 2. 文字列から「大阪」を取り出しなさい。
$birth = '出身は大阪です';
echo mb_substr($birth, 3, 2);
echo '<br>';



// 3. 文字列の「出身」を「生まれ」に置換しなさい。
$birth = '出身は大阪です';
echo str_replace('出身', '生まれ', $birth);
echo '<br>';



// 4. 正規表現を使って文字列「123-4567」の検索をしなさい。
$address = '123-4567 大阪府大阪市...';
$matched = [];
preg_match('/\A[0-9]{3}\-[0-9]{4}/u', $address, $matched);
echo $matched[0];
echo '<br>';



// 5. 正規表現を使って文字列の「.」を「-」に置換しなさい。
$diary = '2025.08.27 今日の授業はPHPです。';
$diary = preg_replace('/([0-9]{4})\.([0-9]{2})\.([0-9]{2})/u', '${1}-${2}-${3}', $diary);
echo $diary;
echo '<br>';



// 6. 現在の日時を取得しなさい。
// 実行イメージ 現在の日時：2025-08-27 13:00:00
date_default_timezone_set('Asia/Tokyo');
echo date('Y-m-d H:i:s');
echo '<br>';



// 7. 最大値最小値を取り出しなさい。
$numbers = [20, 90, 45, 35, 60, 100, 70, 85, 40];
$max = max($numbers);
$min = min($numbers);
echo "最大値：{$min}";
echo '<br>';
echo "最小値：{$max}";
echo '<br>';




// 8.「15000」を桁区切り表記の「15,000」に変換しなさい。
$num = 15000;
echo number_format($num);
echo '<br>';



// 9.「3.14159265359」を四捨五入して小数点以下4桁にしなさい。
$num = 3.14159265359;
echo round($num, 4, PHP_ROUND_HALF_UP);
echo '<br>';



// 10. 配列の要素数を調べなさい。
$fruits = ['apple', 'orange', 'lemon'];
echo count($fruits);
echo '<br>';



// 11. 配列の要素を昇順ソートで並び替えなさい。
$prices = [200, 1800, 150, 2500, 90];
sort($prices);
print_r($prices);
echo '<br>';

// 12. 文字列を「-」で分割し、その結果を配列で受け取りなさい。
$today = '2025-08-27';
$divided_str = explode('-', $today);
print_r($divided_str);
echo '<br>';



// 13. 文字列に日本語が含まれていたら「日本語文字含む」、含まれていない場合は「日本語文字含まない」と表示しなさい。
$str = '私は日本人です';
if (preg_match('/[ぁ-んァ-ヶー 一-龠]/u', $str)) {
    echo '日本語文字含む';
} else {
    echo '日本語文字含まない';
}
echo '<br>';

?>