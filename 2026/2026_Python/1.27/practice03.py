from itertools import count


class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print("...")

class Dog(Animal):
    def speak(self):
        print(f"{self.name}：ワン")

class Cat(Animal):
    def speak(self):
        print(f"{self.name}：ニャー")

animals = []

animals.append(Dog("ポチ"))
animals.append(Dog("シロ"))
animals.append(Cat("タマ"))
animals.append(Cat("ミケ"))

for animal in animals:
    animal.speak()
