### mydata_test.py
"""
Datalogクラス継承
ログの内容を表示する機能を追加
"""
# モジュール
## 継承するクラスをインポートする
from datalog import Datalog

class Mydata(Datalog):

    # 追加機能
    def printlog(self):
        for date, data in self.loglist:
            print(date, data)
        
# Mydataクラスのインスタンスを生成
obj = Mydata()

# スーパークラスから継承したメソッド
obj.log("あいうえお") ### 2026-01-20 10:03:45.161664 あいうえお
obj.log("abcde") ### 2026-01-20 10:03:45.161678 abcde
obj.log(12345) ### 2026-01-20 10:03:45.161679 12345

# 追加したメソッド
obj.printlog()