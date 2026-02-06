### practice.py
"""問題1
Animalクラスを定義
・speak()メソッドを持つ

Dogクラスを定義
・Animalクラスを継承
・speak()メソッドをオーバーライドして"ワン！"と表示させる
"""

class Animal:
    def speak(self):
        pass
    
class Dog(Animal):
    def speak(self):
        print("ワン！")

dog = Dog()
dog.speak()

animal = Animal()
animal.speak() ### なにも出てこない

"""問題2
Personクラスを定義
・greet()メソッドを定義して"Hello"を表示させる。

StudentクラスをPersonクラスを継承して定義
・greet()メソッドをオーバーライドして"I'm a student."と表示させる。
・オーバーライドしたgreet()メソッドでは、Personクラスのgreet()の内容も表示させる。

[表示結果]
Hello
I'm a student.
"""
class Person:
    def greet(self):
        print("Hello")

class Student(Person):
    def greet(self):
        super().greet()
        print("I'm a student.")

person = Student()
person.greet()