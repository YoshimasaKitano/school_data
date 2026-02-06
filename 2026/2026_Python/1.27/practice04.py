class BankAccount:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        if amount < 0:
            print("エラー：入金額は1以上である必要があります。")
            pass

        else:
            self.balance += amount
            print(f"{self.owner}さんの口座に{amount}円を入金しました。")

    def withdraw(self, amount):
        if amount > self.balance:
            print("エラー：残高不足のため出金できません。")
        
        else:
            self.balance -= amount
            print(f"{self.owner}さんの口座から{amount}円を出金しました。")

    def __str__(self):
        return f"{self.owner}:{self.balance}円"
    
account1 = BankAccount("田中")
account2 = BankAccount("佐藤")

account1.deposit(1000)
account1.withdraw(300)
print(account1.__str__())

account2.deposit(500)
account2.withdraw(800)
account2.deposit(200)
print(account2.__str__())