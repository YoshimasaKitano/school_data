### practice05.py
"""
摂氏温度と華氏温度の相互変換、および氷点下判定を行う
"""
class Temperature:

    # 初期化
    def __init__(self, celsius):
        self.celsius = celsius

    # インスタンスメソッド
    def to_fahrenheit(self):
        # 摂氏 → 華氏の変換式
        return self.celsius * (9/5) + 32
    
    # クラスメソッド
    @classmethod
    def from_fahrenheit(cls, f):
        # 華氏 → 摂氏の変換式
        c = (f - 32) * (5/9)
        return cls(c)
    
    # スタティックメソッド
    @staticmethod
    def is_freezing(c):
        # 摂氏温度 c が 0 以下なら True
        return c <= 0
    
# 動作確認
## 摂氏 10°C のインスタンスを作成
t1 = Temperature(10)

## 華氏 14°F を摂氏に変換しインスタンス生成
t2 = Temperature.from_fahrenheit(14)

print(f"t1 の華氏温度: {t1.to_fahrenheit()}")
print(f"t1 は氷点下か: {Temperature.is_freezing(t1.celsius)}")

print(f"t2 の摂氏温度: {t2.celsius}")
print(f"t2 は氷点下か: {Temperature.is_freezing(t2.celsius)}")

