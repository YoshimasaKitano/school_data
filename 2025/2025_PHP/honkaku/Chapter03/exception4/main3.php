<?php
// メインルーチン
$model = new UserModel();
try {
    $profile = $model->findProfile(1001);
} catch (Exception $exception) {
    echo file_get_contents('error-page-not-found.html'); // エラーページを表示する
    return;
}