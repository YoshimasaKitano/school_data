### sample.py
# Carクラスをインポート
from car import Car

# インスタンスの生成
car1 = Car() # 出荷台数: 1台
car2 = Car("red") # 出荷台数: 2台

# インスタンスの変数(属性)を呼び出す
print(f"car1の番号は{car1.mynumber}、色は{car1.color}、走行距離は{car1.mileage}km") ### car1の番号は1、色はwhite、走行距離は0km

print(f"car2の番号は{car2.mynumber}、色は{car2.color}、走行距離は{car2.mileage}km") ### car2の番号は2、色はred、走行距離は0km

# インスタンス変数の値を更新する
car1.color = "green"
print(f"car1の色は{car1.color}、走行距離は{car1.mileage}km") ### car1の色はgreen、走行距離は0km

# インスタンスメソッドの呼び出し
car1.drive(10)
print(f"car1の色は{car1.color}、走行距離は{car1.mileage}km") ### car1の色はgreen、走行距離は10km

car2.drive(15)
print(f"car2の色は{car2.color}、走行距離は{car2.mileage}km") ### car2の色はred、走行距離は15km

# 3台目を出荷
car3 = Car("blue")
print(f"car3の番号は{car3.mynumber}、色は{car3.color}、走行距離は{car3.mileage}km") ### car3の番号は3、色はblue、走行距離は0km

# クラス変数を呼び出す
## インスタンスを生成せずに呼び出せる
print("メーカー:", Car.maker) ### メーカー: NISSAN
print("台数:", Car.count) ### 台数: 0

# クラスメソッドの呼び出し
Car.countup() ### 出荷台数: 1台