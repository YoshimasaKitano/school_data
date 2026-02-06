### practice01.py
"""
四角形の幅と高さを管理し、面積と周囲⻑を計算する。
"""
# クラスの定義
class Rectangle:

    # 初期化設定:属性を定義
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # インスタンスメソッドを定義
    ## 面積を返す
    def area(self):
        return self.width * self.height

    ## 周囲長を返す
    def perimeter(self):
        return (self.width + self.height) * 2


# 動作確認
## インスタンスを生成
rect = Rectangle(5, 3)

## インスタンス変数の取得
print(f"幅:{rect.width}")
print(f"高さ:{rect.height}")

## インスタンスメソッドの呼出し
print(f"面積:{rect.area()}")
print(f"周囲長:{rect.perimeter()}")
