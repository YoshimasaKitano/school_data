## 問題１
# 金額の生成
# from random import randint
# money = randint(1000,10000)
# print("金額：" + str(money))

# # 500円の枚数
# m500 = money // 500

# # 残数
# money %= 500

# # 100円の枚数
# m100 = money // 100

# # 残数
# money %= 100

# # 50円の枚数
# m50 = money // 50

# # 残数
# money %= 50

# # 10円の枚数
# m10 = money // 10

# # 残数
# money %= 10

# # 5円の枚数
# m5 = money // 5

# # 残数
# money %= 5

# # 1円の枚数
# m1 = money // 1

# 表示処理
# print("500円硬貨は" + str(m500) + "枚")
# print("100円硬貨は" + str(m100) + "枚")
# print("50円硬貨は" + str(m50) + "枚")
# print("10円硬貨は" + str(m10) + "枚")
# print("5円硬貨は" + str(m5) + "枚")
# print("1円硬貨は" + str(m1) + "枚")

## 問題2
# count = 1
# result = 0
# while count < 6:
#     text = input("文字を入力")
#     if len(text) == 0:
#         print("**入力エラー")
#         continue
#     else:
#         result += len(text)
#         count += 1
# print("入力合計文字数は、{}文字です。".format(result))

## 問題3
# h = 0
# w = 0
# try:
#     h = float(input("身長(cm)を入力："))
#     if 100 <= h <= 200:
#         w = float(input("体重(kg)を入力："))
#         if 20 <= w <= 100:
#             h_m = h / 100
#             bmi = w / (h_m * h_m)
#             bmi = round(bmi * 100) / 100
#             if bmi < 18:
#                 body = "やせ型"
#             elif 18 <= bmi < 25:
#                 body = "標準型"
#             elif 25<= bmi < 30:
#                 body = "肥満型"
#             elif bmi >= 30:
#                 body = "重度肥満型"
#             print(f"BMI値：{bmi}")
#             print(f"体系：{body}")
#         else:
#             print("不正な値が入力されました。")
#     else:
#         print("不正な値が入力されました。")
# except:
#     print("不正な値が入力されました。")

## 問題4
for i in range(6,0,-1):
    if i == 1:
        print("1階フロント/ロビー")
        continue
    if i == 6:
        print("6階レストラン")
        continue
    print(f"{i}階" , end = "")
    for j in range(1,8):
        if (i == 4 and j == 2) or (i == 4 and j == 4):
            print("[S-S]", end = "")
            continue
        print(f"[{i}-{j}]", end = "")
    print()