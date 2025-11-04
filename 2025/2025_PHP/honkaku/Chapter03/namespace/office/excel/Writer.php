<?php
declare(strict_types=1);

namespace Office\Excel;

// Excelファイルの書き出しクラス
class Writer
{
    // Excelファイルに書き出すメソッド
    public function write(): void
    {
        echo 'Excelファイルを書き出します。', PHP_EOL;
    }
}