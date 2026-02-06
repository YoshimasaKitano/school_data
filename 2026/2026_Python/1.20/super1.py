### super1.py
"""
初期化メソッドの引数
"""
# スーパークラス
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# インスタンスの生成
p1 = Person("大谷翔平", 31)
print(p1.name, p1.age) ### 大谷翔平 31

# サブクラス
class Player(Person):
    def __init__(self, number, position):
        self.number = number
        self.position = position

p2 = Player(17, "ピッチャー")
print(p2.number, p2.position) ### 17 ピッチャー

# サブクラス
class Player2(Person):
    def __init__(self, name, age, number, position):
        super().__init__(name, age) # スーパークラスの初期化メソッド
        self.number = number
        self.position = position
    
    def show(self):
        print("名前：", self.name) ### 大谷翔平
        print("年齢：", self.age) ### 31
        print("背番号：", self.number) ### 17
        print("ポジション：", self.position) ### ピッチャー

p3 = Player2("大谷翔平", 31, 17, "ピッチャー")
print(p3.name, p3.age, p3.number, p3.position) ### 大谷翔平 31 17 ピッチャー
p3.show()
"""
名前： 大谷翔平
年齢： 31
背番号： 17
ポジション： ピッチャー
"""