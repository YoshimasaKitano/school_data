# while_sample2.py
"""
while文のネスト
"""

i = 1
while i <= 5:
    print("i =",i)

    j = 0
    while j < 3:
        print (" j =",j)
        j += 1

    i += 1

else:
    print("終了")

"""練習
＠＠＠＠＠
＠＠＠＠＠
＠＠＠＠＠
＠＠＠＠＠
＠＠＠＠＠
"""
t = 0
while t < 5:

    y = 0
    while y < 5:
        print("＠",end = "")
        y += 1

    print()

    t += 1

"""九九の表

"""

t = 1
while t < 10:

    y = 1
    while y < 10:

        result = t * y

        print(result,end = " ")
        y += 1

    print()

    t += 1

"""三角形

＠
＠＠
＠＠＠
＠＠＠＠
＠＠＠＠＠

"""

"""逆三角形
＠＠＠＠＠
＠＠＠＠
＠＠＠
＠＠
＠
"""

t = 0
z = 1
while t < 5:
    
    y = 0
    while y < z:
        print("＠",end = "")
        y += 1

    z += 1

    print()

    t += 1

t = 0
while t < 6:

    y = 0
    while y < t:
        print("＠",end = "")
        y += 1

    print()

    t += 1

t = 0
z = 5
while t < 5:
    
    y = 0
    while y < z:
        print("＠",end = "")
        y += 1

    z -= 1

    print()

    t += 1 

t = 0
while t < 6:

    y = 5
    while y > t:
        print("＠",end = "")
        y -= 1

    print()

    t += 1