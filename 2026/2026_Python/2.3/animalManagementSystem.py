from abc import ABC, abstractmethod
class Animal(ABC):

    _count = 0

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):

        if len(name) == 0:
            print("空文字は指定できません。")
            raise ValueError
        
        self._name = name
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):

        if age <= 0:
            print("年齢は0歳より上で指定してください")
            raise ValueError

        self._age = age
    
    @abstractmethod
    def speak(self):
        raise NotImplementedError

    @classmethod
    def get_animal_count(cls):
        return cls._count
    
    @staticmethod
    def is_adult(age):
        if age >= 3:
            return "大人"
        else:
            return "子供"

class Dog(Animal):
    def __init__(cls, name, age):
        super().__init__(name, age)
        Animal._count += 1
    
    def speak(self):
        return "ワン！"

class Cat(Animal):
    def __init__(cls, name, age):
        super().__init__(name, age)
        Animal._count += 1

    def speak(self):
        return "ニャー！"

dog = Dog("ポチ", 1)
cat = Cat("チップ", 2)

print(f"{dog.name}の鳴き声は{dog.speak()}で、年齢は{dog.age}歳なので{Animal.is_adult(dog.age)}です。")
print(f"{cat.name}の鳴き声は{cat.speak()}で、年齢は{cat.age}歳なので{Animal.is_adult(cat.age)}です。")
dog.name = "ハチ"
cat.age = 5
print(f"犬の新しい名前: {dog.name}")
print(f"猫の年齢: {cat.age}")
print(f"動物の総数: {Animal.get_animal_count()}")