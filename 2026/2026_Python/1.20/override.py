### override.py
"""
オーバーライド:内容の上書き
"""
# スーパークラス
class Greet:
    def hello(self):
        print("やあ！")

    def bye(self):
        print("さよなら")


# サブクラス
class Greet2(Greet):
    # 継承したhello()を上書き
    def hello(self, name = None):
        if name:
            print(f"{name}さん、こんにちは！")
        else:
            # スーパークラスのhello()を使う
            super().hello()

obj1 = Greet()
obj1.hello() ### やあ！

obj2 = Greet2()
obj2.hello() ### やあ！
obj2.bye() ### さよなら

obj2.hello("竹國") ### 竹國さん、こんにちは！

"""
オーバーロード：メソッドの重複定義
"""
class Greet3:
    def hello(self, name = None):
        print(f"{name}さん、こんにちは！")
    
    def hello(self): # 上部のhello()を上書き
        print("やあ！")

obj3 = Greet3()
# obj3.hello("丸山") ### 丸山さん、こんにちは！

"""
スーパークラスのメソッドに追加する
"""
class Greet4(Greet):
    def hello(self):
        super().hello()
        print("元気？") # 追加分

obj4 = Greet4()
obj4.hello()
"""
やあ！
元気？
"""  