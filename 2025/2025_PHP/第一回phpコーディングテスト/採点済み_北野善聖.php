<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>2025PHP基礎構文テスト</title>
</head>
<body>
   <?php

   /**
    * PHP基礎構文テスト
    * 問題文をよく読んで解答しなさい。
    * 
    * 注意事項
    * 実行イメージの表記がある場合はそのとおりに解答すること。
    * 変数名は意味の伝わるものにすること。
    * インデントは正確に設定すること。
    * 半角スペースは適切に入れること。
    * 問題ごとに[echo '<br>']で改行すること。（それ以外の改行コードは使わない）
    * エラーが出ても考え方が合っていれば加点の可能性があるので、
    * コードは消さずにコメントアウトで残すこと。
    * 「配列を定義しなさい」 → (例)$array = [] とし、代入は次の処理でおこなう。
    */

   // 問1. 変数を使って自分の名前を表示しなさい。（各1点）
   // 実行イメージ　　私の名前は○○です（全角フルネームスペースなし）
   // 採点3点

   // 連結出力
   $name = '北野善聖';
   echo '私の名前は' .$name .'です';
   echo '<br>';

   // 次々出力
   echo '私の名前は', $name, 'です';
   echo '<br>';

   // 変数展開出力
   echo "私の名前は{$name}です";
   echo '<br>';

   
   // 問2. 定数命令を使って、1,000円の商品を購入した時の税込価格（消費税率10%）を計算しなさい。（2点）
   // 実行イメージ　　税込み1100円
   // 採点2点
   
   $result = 0;
   define('TAX', 0.1);
   $result = (TAX * 1000) + 1000;
   echo "税込み{$result}円";
   echo '<br>';


   // 問3. if命令と比較演算子を使って厳密な判断をし、結果を表示しなさい。パスワード（$password）と確認用パスワード（$password_conf）が一致していたら「パスワードは一致している」、一致していなかったら「パスワードは一致していない」とする。if-elseではなくif-ifの形式とする。（5点）
   // 実行イメージ　　パスワードは一致している
   // 採点5点
   
   $password = 12345;
   $password_conf = 12345;
   if ($password === $password_conf) {
      echo 'パスワードは一致している';
   }
   if ($password !== $password_conf) {
      echo 'パスワードは一致していない';
   }
   echo '<br>';


   // 問4. if命令を使ってテストの点数を評価しなさい。90点以上なら「評価A」、70点以上なら「評価B」、50点以上なら「評価C」、それ以外は「追試D」とする。（5点）
   // 実行イメージ　　評価A
   // 採点5点
   
   $test = 100;
   if ($test >= 90) {
      echo '評価A';
   } elseif ($test >= 70) {
      echo '評価B';
   } elseif ($test >= 50) {
      echo '評価C';
   } else {
      echo '追試D';
   }
   echo '<br>';


   // 問5. 値が偶数の場合、奇数の場合、0以下の場合を判断し、その結果を表示しなさい。（5点）
   // 実行イメージ　　（値が10の場合）10：偶数　（値が15の場合）15：奇数　（値が0以下の場合）0：0より大きい値を設定してください
   // 採点5点
   
   $num = 3;
   if ($num > 0) {
      if ($num % 2 == 0) {
         echo "{$num}：偶数";
      } else {
         echo "{$num}：奇数";
      }
   } else {
      echo "{$num}：0より大きい値を設定してください";
   }
   echo '<br>';


   // 問6. while命令を使って文字列を5回繰り返して表示しなさい。繰り返しカウンタは$iとする。（5点）
   /* 実行イメージ
   　 PHP復習：1回目
   　 PHP復習：2回目
   　 PHP復習：3回目
   　 PHP復習：4回目
   　 PHP復習：5回目
   */
   // 採点5点
   
   $i = 1;
   while ($i < 6) {
      echo "PHP復習：{$i}回目";
      echo '<br>';
      $i++;
   }



   // 問7. for命令を使って7日目に貯まるお小遣いの合計額を計算しなさい。現在のお小遣いは合計1500円で、1日100円ずつもらえるものとする。繰り返しカウンタは$iとする。（5点）
   // 実行イメージ　　7日目には2200円貯まりました
   // 採点5点
   
   $money = 1500;
   for ($i = 1; $i < 8; $i++) {
      $money += 100;
   }
   echo "7日目には{$money}円貯まりました";
   echo '<br>';


   // 問8. for命令とcount関数を使って、配列 [65, 41, 80, 9, 100] から最大値と最小値を取り出し表示しなさい。（6点）
   /* 実行イメージ
      最大値：100
      最小値：9
   */
   // 採点6点
   
   $nums = [65, 41, 80, 9, 100];
   $min = $nums[0];
   $max = $nums[0];
   for ($i = 1; $i < count($nums); $i++) {
      if ($min > $nums[$i]) {
         $min = $nums[$i];
      }
      if ($max < $nums[$i]) {
         $max = $nums[$i];
      }
   }
   echo "最大値：{$max}";
   echo '<br>';
   echo "最小値：{$min}";
   echo '<br>';


   // 問9. 配列$argsに文字列'10'と'20'を代入しなさい。添字を指定し代入すること。また、配列の文字列を数値に型変換（型キャスト）させて、計算結果を表示しなさい。（6点）
   // 実行イメージ　　10+20=30
   // 採点6点
   
   $args = [];
   $result = 0;
   $args[0] = '10';
   $args[1] = '20';
   $args1 = (int)$args[0];
   $args2 = (int)$args[1];
   $result = $args1 + $args2;
   echo "{$args1}+{$args2}={$result}";
   echo '<br>';


   // 問10. for命令とcontinue命令を使って、1～100までの偶数の合計を計算しなさい。（6点）
   // 実行イメージ　　偶数の合計値は2550です
   // 採点6点
   
   $result = 0;
   for ($i = 1; $i < 101; $i++) {
      if ($i % 2 != 0) {
         continue;
      }
      $result += $i;
   }
   echo "偶数の合計値は{$result}です";
   echo '<br>';


   // 問11. foreach命令とリファレンス渡しを使って配列の値を一律に2倍に計算し表示しなさい。unset関数の処理を忘れないこと。（6点）
   // 実行イメージ　　Array ( [0] => 20 [1] => 60 [2] => 120 )
   // 採点6点
   
   $nums = [10, 30, 60];
   foreach ($nums as &$num) {
      $num *= 2;
   }
   unset($num);
   print_r($nums);
   echo '<br>';


   // 問12. 年齢が0歳以上かつ12歳以下は入園料が「乳児・幼児特別招待」、13歳以上かつ60歳以下の方は「入園料2000円」、61歳以上は「入園料1000円」と表示しなさい。（6点）
   // 実行イメージ　　乳児・幼児特別招待
   // 採点6点
   
   $age = 10;
   if ($age > 0 && $age <= 12) {
      echo '乳児・幼児特別招待';
   } elseif ($age >= 13 && $age <= 60) {
      echo '入園料2000円';
   } elseif ($age >= 61) {
      echo '入園料1000円';
   }
   echo '<br>';


   // 問13. 配列$fruitsを定義し値を代入しなさい。添字を指定し代入すること。実行イメージのとおり結果を出力しなさい。（6点）
   // 実行イメージ　　Array ( [0] => apple [1] => orange [2] => lemon )
   // 採点6点
   
   $fruits = [];
   $fruits[0] = 'apple';
   $fruits[1] = 'orange';
   $fruits[2] = 'lemon';
   print_r($fruits);
   echo '<br>';


   // 問14. 連想配列$usersを定義し値を代入しなさい。また、$keyと$valueを使って値を出力しなさい。（6点）
   /* 実行イメージ
      name - 山田
      age - 20
      address - 大阪
   */
   // 採点6点
      
   $users = [];
   $users['name'] = '山田';
   $users['age'] = 20;
   $users['address'] = '大阪';
   foreach ($users as $key => $value) {
      echo "{$key} - {$value}";
      echo '<br>';
   }



   // 問15. 配列$scoresにある値を使って点数に応じた成績付けをしなさい。90点以上は評価A、70点以上は評価B、50点以上は評価C、それ以外は評価Dとする。（8点）
   /* 実行イメージ
      95点 : 評価A
      67点 : 評価C
      58点 : 評価C
      82点 : 評価B
      76点 : 評価B
      40点 : 評価D
   */
   // 採点8点

   $scores = [95, 67, 58, 82, 76, 40];
   for ($i = 0; $i < count($scores); $i++) {
      if ($scores[$i] >= 90) {
         echo "{$scores[$i]}点 : 評価A";
         echo '<br>';
      } elseif ($scores[$i] >= 70) {
         echo "{$scores[$i]}点 : 評価B";
         echo '<br>';
      } elseif ($scores[$i] >= 50) {
         echo "{$scores[$i]}点 : 評価C";
         echo '<br>';
      } else {
         echo "{$scores[$i]}点 : 評価D";
         echo '<br>';
      }
   }





   // 問16. 【自由プログラミング】PHPプログラミングを学び、習得できたスキルを自己アピールしなさい。※記述方式にルールはありません。（20点）
   // 例1：コメントによる文章
   // 例2：プログラムコード
   // 例3：HTMLとCSSを使った実装など
   // 採点20点

   // if文の複数の条件式を一つにまとめる
   $language = 'HTML';
   if ($language == 'HTML' || $language == 'CSS' || $language == 'JavaScript') {
      echo 'クライアントサイド言語';
   } elseif ($language == 'PHP' || $language == 'Java') {
      echo 'サーバーサイド言語';
   }
   echo '<br>';

   // 連想配列をforeachを使ってmathとenglishの合計値と平均値を出してから出力する。
   $result = 0;
   $average = 0;
   $students = [
      [
         'name' => 'たろう',
         'age' => 19,
         'math' => 30,
         'english' => 50,
      ],
      [
         'name' => 'はなこ',
         'age' => 18,
         'math' => 45,
         'english' => 75, 
      ]
   ];
   foreach ($students as $student) {
      $result = $student['math'] + $student['english'];
      $average = $result / 2;
      echo "{$student['name']} - 合計:{$result}, 平均:{$average}";
      echo '<br>';
   }

   // 連想配列をループ処理を使わずにmathとenglishの合計値と平均値を出してから出力する。
   $students = [
      [
         'name' => 'たろう',
         'age' => 19,
         'math' => 30,
         'english' => 50,
      ],
      [
         'name' => 'はなこ',
         'age' => 18,
         'math' => 45,
         'english' => 75, 
      ]
   ];
   $students[0]['result'] = $students[0]['math'] + $students[0]['english'];
   $students[1]['result'] = $students[1]['math'] + $students[1]['english'];
   $students[0]['average'] = $students[0]['result'] / 2;
   $students[1]['average'] = $students[1]['result'] / 2;
   echo "{$students[0]['name']} - 合計:{$students[0]['result']}, 平均:{$students[0]['average']}";
   echo '<br>';
   echo "{$students[1]['name']} - 合計:{$students[1]['result']}, 平均:{$students[1]['average']}";
   echo '<br>';

   // phpタグを閉じずに改行しながらそのまま出力する。
   $numbers = [10, 20, 30, 40, 50];
   echo '<pre>';
   print_r($numbers);
   echo '</pre>';
   echo '<br>';

   // switch構文を使って条件分岐させる。
   $menu = 'サンドイッチ';
   switch($menu) {
      case 'ハンバーガー':
         echo '500円です';
         break;
      case 'サンドイッチ':
         echo '300円です';
         break;
      case 'ポテト':
      case 'チキンナゲット':
         echo '150円です';
         break;
      default :
         echo 'メニューから選んでください';
   }
   echo '<br>';




   /*
   *
   *   採点合計　100点！
   * 
   * 　100点満点素晴らしいです！よく頑張りました！
   * 　日頃の授業に対する姿勢が素晴らしいです！
   * 　今後を楽しみにしています！
   * 　
   *   PHPプログラミング基礎構文テストはこれで終了です。
   * 　お疲れさまでした。
   * 
   * 　PHPプログラミング基礎　織田
   * 　注意！PHP織田の授業で使用したデータや資料全てを、他の人に見せたり渡したりしないようにお願いします。
   */



   ?>
</body>
</html>