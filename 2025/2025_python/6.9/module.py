# module.py
"""
モジュールを読み込む
"""
# モジュールのインポート
import math

# モジュールを使う
print(math.ceil(3.14)) ### 4 # 小数点で切り上げ
print(math.floor(3.14)) ### 3 # 小数点で切り捨て

# mathモジュールが持つ定数
print(math.pi) ### 3.141592653589793 円周率

print(math.degrees(math.pi/4)) ### 45.0

"""
木までの距離と角度から木の高さを求める
"""
kyori = 20
kakudo = math.radians(32)
takasa = kyori * math.tan(kakudo)
print(takasa) ### 12.497387038186549

takasa = math.floor(takasa * 100) /100

print(takasa) ### 12.49
print(str(takasa) + "m") ### 12.49m

## 関数を指定してモジュールを読み込む
"""
import random # 乱数に関するモジュール

num = random.randint(1,6) # 1から6の整数の乱数を生成する
print(num)
"""

from random import randint

num = randint(1,6) # 1から6の整数の乱数を生成する
print(num)

# 読み込む関数に名前をつける
from random import randint as dice
print(dice(1,6))
