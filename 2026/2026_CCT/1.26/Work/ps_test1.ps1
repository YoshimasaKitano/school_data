for ($i = 1; $i -le 100; $i++)
{
    Write-Progress "PowerShellスクリプトファイルの練習です" "進捗状況:" -PercentComplete $i
    Start-Sleep -Milliseconds 100
}