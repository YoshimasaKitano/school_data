### polymorphism.py
"""
多態性(ポリモフィズム)
"""
class Dog:
    def speak(self):
        return "ワン!"

class Cat:
    def speak(self):
        return "ニャー!"

# インスタンスの生成
dog = Dog()
cat = Cat()

speak_dog = dog.speak()
print(speak_dog) ### ワン!

speak_cat = cat.speak()
print(speak_cat) ### ニャー!

def animal_speak(animal):
    print(animal.speak())

animal_speak(dog) ### ワン!
animal_speak(cat) ### ニャー!