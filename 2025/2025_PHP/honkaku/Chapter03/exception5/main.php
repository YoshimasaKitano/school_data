<?php
try {
    // 例外を起こすために故意に</data>を</DATA>と書いています。
    $parsedXml = new SimpleXMLElement('<xml><data>XML DATA</DATA></xml>');
    echo $parsedXml->data;
} catch (Exception $exception) {
    echo '例外をキャッチしました。エラー内容：', $exception->getMessage();
}