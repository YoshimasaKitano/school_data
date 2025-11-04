### calc.py
## BMIの演算を行うモジュール
# bmiの計算の関数calc_bmi()
def calc_bmi(h, w):
    bmi = w / ((h / 100) * (h / 100))
    bmi = round(bmi, 2)
    return bmi

# 体型判定の関数body_type()
def body_type(bmi):
    body = ""
    if bmi < 18:
        body = "やせ型"
    elif bmi < 25:
        body = "標準型"
    elif bmi < 30:
        body = "肥満型"
    else:
        body = "重度肥満型"
    return body
