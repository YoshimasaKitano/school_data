### exchange.py
## 関数を定義したモジュールファイル
# 円→ドルに換算する
def yen2dollar(yen, rate, charge=0):
    dollar = yen / (rate + charge)
    return dollar

# ドル→円に換算する
def dollar2yen(dollar, rate, charge):
    yen = dollar * (rate - charge)
    return yen