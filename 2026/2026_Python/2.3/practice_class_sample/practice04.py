### practcie04.py
"""
銀行口座を表す BankAccount クラスを示す。
口座名義と残高を保持し、入金・出金・残高表示など口座操作
"""
class BankAccount:

    # 初期化　口座名と残高　残高は初期値 0
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0

    # 指定金額を残高に加算
    def deposit(self, amount):

        # バリデーション
        if amount <= 0:
            print("エラー︓入金額は 1 以上である必要があります")
            return  # 処理を終了させる

        # 入金処理(加算)
        self.balance += amount
        print(f"{self.owner} さんの口座に {amount} 円を入金しました。")

    #  指定金額を残高から減算する。残高不足の場合はエラー表示
    def withdraw(self, amount):

        # バリデーション
        if amount > self.balance:
            print("エラー︓残高不足のため出金できません。")
            return

        # 出金処理(減算)
        self.balance -= amount
        print(f"{self.owner} さんの口座に {amount} 円を出金しました。")

    # 文字列化(特殊メソッド)
    def __str__(self):
        return f"{self.owner} : {self.balance}円"

# 動作確認
## インスタンスを生成
account1 = BankAccount("田中")
account2 = BankAccount("佐藤")

## 田中さんの口座
account1.deposit(1000)  # 入金処理
account1.withdraw(300)  # 出金処理
print(account1)

## 佐藤さんの口座
account2.deposit(500)
account2.withdraw(800)
account2.deposit(200)
print(account2)
