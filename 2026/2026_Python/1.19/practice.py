### practice.py
"""練習問題1
Personクラスを定義
・属性に名前(name)と年齢(age)を持つ
・info()メソッドで「私の名前は〇〇で、年齢は〇歳です。」と表示する。

Personクラスのインスタンスを生成して例のように表示させる。
(例)私の名前は大谷翔平で、年齢は31歳です。
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def info(self):
        print((f"私の名前は{self.name}で、年齢は{self.age}です。"))

person1 = Person("大谷翔平", 31)
person1.info()

"""練習問題2
Rectangleクラスを定義
・属性に幅(width)、高さ(height)を持つ
・area()メソッドで面積を返す

引数に3, 5を渡し、Rectangleクラスのインスタンスを生成する
area()メソッドを呼び出して値を取得、例のように表示させる
(例)面積は35です。
"""

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

area1 = Rectangle(3, 5)
print(f"面積は{area1.area()}です。")
