### mymoney.py
## 為替の計算を行う
# モジュールの読み込み
import exchange
import function_practice01

yen = 25000
rate = 147.27
charge = 1.0

dollar = exchange.yen2dollar(yen, rate, charge)
print(f"本日の為替：{yen}は、{dollar:,.2f}ドル") ### 本日の為替：25000は、168.61ドル

dollar = 5.79

yen = exchange.dollar2yen(dollar, rate, charge)
print(f"アメリカのBigMac{dollar}ドルは、日本円で{yen:,.2f}円") ### アメリカのBigMac5.79ドルは、日本円で846.90円