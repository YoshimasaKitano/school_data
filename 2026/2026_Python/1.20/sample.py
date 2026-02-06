### sample.py
"""
クラスの継承
"""
# スーパークラスの定義
class A:
    # インスタンスメソッド
    def hello(self):
        print("ハロー")

a = A()
a.hello() ### ハロー
# a.bye() ### エラー:'A' object has no attribute 'bye'

# Aクラスを継承してBクラス(サブクラス)を定義
class B(A):
    def bye(self):
        print("グッバイ")

b = B()
b.hello() ### ハロー Aから継承したメソッド
b.bye() ### グッバイ

# Aクラスを継承してCクラスを定義
class C(A):
    pass

c = C()
c.hello() ### ハロー

# Bクラスを継承してDクラスを定義
class D(B):
    pass

d = D()
d.hello() ### ハロー
d.bye() ### グッバイ