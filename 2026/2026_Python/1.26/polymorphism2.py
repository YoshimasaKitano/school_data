### polymorphism2.py
"""
継承を使った多態性(ポリモフィズム)
"""
# 親クラス
class Animal():
    def speak(self):
        # raiseを使って中身のないメソッドを定義
        raise NotImplementedError

# a = Animal()
# print(a.speak()) ### エラー:NotImplementedError

# 子クラス
class Dog(Animal):
    # オーバーライド
    def speak(self):
        return "ワン!"

class Cat(Animal):
    # オーバーライド
    def speak(self):
        return "ニャー!"

# インスタンスの生成
dog = Dog()
cat = Cat()

print(dog.speak()) ### ワン!
print(cat.speak()) ### ニャー!