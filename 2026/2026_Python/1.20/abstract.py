### abstract.py
"""
抽象クラス・抽象メソッド
"""
"""問題1
Animalクラスを定義
・speak()メソッドを持つ

Dogクラスを定義
・Animalクラスを継承
・speak()メソッドをオーバーライドして"ワン！"と表示させる
"""
from abc import ABC, abstractmethod

# 抽象クラス
class Animal(ABC):

    # 抽象メソッド
    @abstractmethod
    def speak(self):
        pass
    
# 抽象クラスを継承することで抽象メソッドを実装する必要がある
class Dog(Animal):
    def speak(self):
        print("ワン！")

dog = Dog()
dog.speak()

# 抽象クラスのインスタンスは生成できない
# animal = Animal() ### エラーになる
# animal.speak()