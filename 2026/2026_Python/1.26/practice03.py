class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print("...")

class Dog(Animal):
    def speak(self):
        print("ワン")

class Cat(Animal):
    def speak(self):
        print("ニャー")

animal = []

animal.append(Dog("ポチ").speak())
animal.append(Dog("シロ").speak())
animal.append(Cat("タマ").speak())
animal.append(Cat("ミケ").speak())

