### simple.py

# simpleクラスを定義
class Simple:
    pass

# クラスにメンバーを追加する
# クラス変数xを追加
Simple.x = 100
print(Simple.x) ### 100
print(Simple.x* 2) ### 2000

# クラスメソッドを定義
## 関数定義
def hello(msg = "ハロー！"):
    print(msg)

## greetingクラスメソッド
Simple.greeting = hello

## クラスメソッドの呼び出し
Simple.greeting("おはよう！") ### おはよう！

Simple.greeting() ### ハロー！

"""ここまでのSimpleクラスのイメージ
class Simple:
    x = 100

    def greeting(msg = "ハロー！")
        print(msg)
"""

# インスタンスメンバーの追加
## インスタンスの生成
obj = Simple()

## インスタンス変数 a を追加
obj.a = 123
print(obj.a) ### 123

# インスタンスメソッドを追加
## メソッドの定義
def drum(beat = "ドコドコ"):
    print(beat)

def sax(phrase = "ブーブー"):
    print(phrase)

## インスタンスに追加
obj.play = drum

## インスタンスメソッドの呼び出し
obj.play() ### ドコドコ

obj2 = Simple()
obj2.play = sax
obj2.play() ### ブーブー
# print(obj2.a) # エラー: obj2には変数aは追加されていないため

"""ここまでのSimpleクラスのイメージ
class Simple:
    x = 100

    def greeting(msg = "ハロー！")
        print(msg)

    def __init__(self): # obj2にはない
        self.a = 123
    
    def play(self, beat):
        print(beat)
"""

# 追加したメンバーを削除
## インスタンスメンバーの作成
obj.a = None
obj.play = None

print(obj.a) ### None
# obj.play() ### エラー: 'NoneType' object is not callable

## クラス変数の削除
del Simple.x
# print(Simple.x) ### エラー: type object 'Simple' has no attribute 'x'