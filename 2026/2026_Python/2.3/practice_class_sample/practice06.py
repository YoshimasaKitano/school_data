### practice06.py
"""
抽象クラスを用いて共通インターフェースを定義
具象クラスで実装する
"""
from abc import ABC, abstractmethod

# 図形の抽象クラス
class Shape(ABC):

    # 抽象メソッド:面積を返す
    @abstractmethod
    def area(self):
        pass

    # 抽象メソッド:周囲長を返す
    @abstractmethod
    def perimeter(self):
        pass

# 具象クラスで実装
class Circle(Shape):
    # 初期化
    def __init__(self, radius):
        self.radius = radius

    # 円の面積
    def area(self):
        return 3.14 * self.radius ** 2 
    
    # 円の周囲長
    def perimeter(self):
        return 2 * 3.14 *  self.radius
    
class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    # 四角形の面積
    def area(self):
        return self.width * self.height
    
    # 四角形の周囲長
    def perimeter(self):
        return (self.width + self.height) * 2
    
# 動作確認
shapes = [
    Circle(3),
    Rectangle(4,5),
    Circle(1),
    Rectangle(2,6)
]

# ※値を小数点第２まで出力
for shape in shapes:
    print(f"{shape.__class__.__name__} → 面積: {shape.area():.2f}, 周囲⻑: {shape.perimeter():.2f}")
