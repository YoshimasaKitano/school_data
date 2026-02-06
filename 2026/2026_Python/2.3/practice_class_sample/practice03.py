### practice03.py
"""
動物を表す Animal クラスを基底クラスとし、
犬（Dog）と猫（Cat）を継承によって実装する
共通のインターフェース speak() を通じて
異なる鳴き声を返す
"""

class Animal:

    ## 初期化設定:属性を定義
    def __init__(self, name):
        self.name = name

    ## インスタンスメソッドの定義
    def speak(self):
        return "..."
    
class Dog(Animal):

    # 親クラスのメソッドをオーバーライド(上書き処理)
    def speak(self):
        return "ワン"
    
class Cat(Animal):

    # 親クラスのメソッドをオーバーライド(上書き処理)
    def speak(self):
        return "ニャー"
    
# 動作確認
## インスタンスをリスト化
animals = [
    Dog("ポチ"),
    Dog("シロ"),
    Cat("タマ"),
    Cat("ミケ"),
]

## 繰り返し各インスタンスから属性とメソッドを取得
for animal in animals:
    print(f"{animal.name}:{animal.speak()}")
    