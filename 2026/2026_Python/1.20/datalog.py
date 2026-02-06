### datalog.py
"""
データとその記録日時を保存する機能
"""
# モジュール
from datetime import datetime

class Datalog:

    def __init__(self):
        self.loglist = [] # ログを保持するリスト
    
    def log(self, data):
        now = datetime.now()
        item = (now, data) # 日時とデータをタプルで保持
        self.loglist.append(item)