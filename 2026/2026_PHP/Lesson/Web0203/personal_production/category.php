<?php 
    declare(strict_types=1); 
    require_once dirname(__FILE__) . '/functions.php';
?>
<?php 
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    
} 
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>カテゴリー一覧</title>
</head>
<body>
    <table border="1">
        <tr>
            <th>テーブルの名前</th>
            <th>中身一覧</th>
            <th>更新</th>
            <th>削除</th>
        </tr>
        <tr>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
    </table>
    <p><a href="index.html">戻る</a></p>
</body>
</html>