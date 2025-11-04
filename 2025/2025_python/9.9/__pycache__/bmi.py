### bmi.py
import calc

try:
    h = float(input("身長(cm)を入力→"))
    w = float(input("体重(kg)を入力→"))

    bmi = calc.calc_bmi(h, w)

    print("BMI値:", bmi)
    print("体型:", calc.body_type(bmi))

except:
    print("エラーが発生しました。")

