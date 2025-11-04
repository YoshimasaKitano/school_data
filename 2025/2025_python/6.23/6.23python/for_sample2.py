# for_sample2.py
"""
break文
"""
# 0から5までカウントアップ表示
# iが3の場合、繰り返しから抜ける
for i in range(6):

    if i == 3:
        break

    print("i=",i)

"""
continue文
"""
# 0から5までカウントアップ表示
# iが3の場合、繰り返しからスキップ
for i in range(6):

    if i == 3:
        continue

    print("i=",i)

"""
繰り返しのネストの場合
break文
"""
# 0から5までカウントアップ表示
# iが3の場合、繰り返しから抜ける
for i in range(3):

    # if i == 1:
    #     break

    print("i=",i)

    for j in range(3):

        if i == 1:
            break

        print(" j=",j)

# 0から5までカウントアップ表示
# iが3の場合、繰り返しから抜ける
for i in range(3):

    # if i == 1:
    #     break

    print("i=",i)

    for j in range(3):

        if i == 1:
            continue

        print(" j=",j)

"""
for in - else文
"""
# 0から9までカウントアップ表示

for i in range(10):

    if i == 5:
        break

    print("i=",i)

else:
    print("最後までカウントしました！")

print("終了")

"""
繰り返しネストの場合
"""
for i in range(5):

    print("i=",i)

    for j in range(5):

        if i == 3:
            break

        print(" j=",j)

    else:
        # print(" jの終了")
        continue

    break

else:
    print("iの終了")