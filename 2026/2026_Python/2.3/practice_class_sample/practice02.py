### practice02.py
"""
数値をカウントするための簡易カウンター機能
カウント値の増加およびリセットを行う
"""
# クラスの定義
class Counter:

    ## 初期化設定:属性を定義
    def __init__(self):
        self.count = 0

    ## インスタンスメソッド:増加処理
    def increment(self):
        self.count += 1

    ## インスタンスメソッド:リセット処理
    def reset(self):
        self.count = 0
   
# 動作確認
## インスタンスの生成
counter = Counter()

## インスタンスの呼出し:増加処理を3回
counter.increment()
counter.increment()
counter.increment()

## インスタンス変数の取得
print(f"現在の値:{counter.count}")

## インスタンスメソッドの呼出し:リセット処理
counter.reset()
print(f"リセット後の値:{counter.count}")
