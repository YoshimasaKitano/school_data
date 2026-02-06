### animalManagementSystem.py
"""
動物管理システム
オブジェクト指向の主要概念をすべて利用したプログラム
"""
from abc import ABC, abstractmethod

# すべての動物の共通基盤となる抽象クラス
class Animal(ABC):

    ## クラス変数
    __count = 0

    ## 初期化設定
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        Animal.__count += 1

    ## 抽象メソッド（子クラスで実装）
    @abstractmethod
    def speak(self):
        pass

    ## ゲッター・セッター（property）
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):

        # バリデーション(空文字禁止)
        if len(value) == 0:
            raise ValueError("空文字禁止")

        self.__name = value

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value):

        # バリデーション(0歳以上)
        if value > 0:
            raise ValueError("0以上のみ許可")
        
        self.__age = value

    ## クラスメソッド
    @classmethod
    def get_animal_count(cls):
        return cls.__count
    
    ## スタティックメソッド
    @staticmethod
    def is_adult(age):
        return age >= 3
    
# Dog（Animal を継承）
class Dog(Animal):
    def speak(self):
        return "ワン!"

# Cat（Animal を継承）
class Cat(Animal):
    def speak(self):
        return "ニャー!"
    
# 動作確認
## 犬と猫のインスタンスを作成
dog = Dog("ポチ", 3)
cat = Cat("たま", 2)

## インスタンスメソッドの呼出し
print(f"{dog.name} : {dog.speak()}")
print(f"{cat.name} : {cat.speak()}")

## セッター、ゲッター
dog.name = "ハチ"
print(f"新しい犬の名前 : {dog.name}")

## スタティックメソッドの呼出し
print(f"{dog.name}は大人か？ : {Animal.is_adult(dog.age)}")
print(f"{cat.name}は大人か？ : {Animal.is_adult(cat.age)}")

## クラスメソッドの呼出し
print(f"動物の総数 : {Animal.get_animal_count()}")

    



