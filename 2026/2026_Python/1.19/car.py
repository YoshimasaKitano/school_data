### car.py
"""
クラスの定義
"""
# Carクラスを定義
class Car: # 自動車を表すクラス

    # クラスメンバー
    # クラス変数を定義
    maker = "NISSAN"
    count = 0

    # クラスメソッド
    @classmethod
    def countup(cls):
        cls.count += 1
        print(f"出荷台数: {cls.count}台")

    # 初期化メソッド
    def __init__(self, color = "white"):
        # 初期化処理
        Car.countup() # クラスメソッドの呼び出し
        self.mynumber = Car.count
        
        self.color = color # self.colorに第二引数のcolorを代入する
        self.mileage = 0
    
    # インスタンスメソッドの定義
    def drive(self, km):
        self.mileage += km