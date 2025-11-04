# python01A_bingo.py
"""
Enterキーを押すと
このクラスの誰かの名前が表示される
"""
import random
input("Enterキーを押してください")
member = ["北野善聖","岡本篤希","清原未瑠","市川春流","荒井智則","石岡由奈","梅津亮介","HARITH DANIELE SEE CHUN","畔上雄大","岩田直樹","河田珂音","門阪優希奈","河野杏奈","大森進太郎","朝来野仁","中西璃","犬童悠之介","堂間蓮太郎","橋口愛"]
member_choice =random.choice(member)
print(member_choice)

"""
模範解答
"""

import random

input("Enter")

name = " "
num = random.randint(1,19)

if num == 1:
    name = "犬童悠之介"
elif num == 2:
    name = "堂間蓮太郎"
elif num == 3:
    name = "中西璃"
elif num == 4:
    name = "橋口愛"
elif num == 5:
    name = "ハリスダニエルシチュンファ"
elif num == 6:
    name = "朝来野仁"
elif num == 7:
    name = "畔上雄大"
elif num == 8:
    name = "荒井智則"
elif num == 9:
    name = "石岡由奈"
elif num == 10:
    name = "市川春流"
elif num == 11:
    name = "岩田直樹"
elif num == 12:
    name = "梅津亮介"
elif num == 13:
    name = "大森進太郎"
elif num == 14:
    name = "岡本篤希"
elif num == 15:
    name = "門阪優希奈"
elif num == 16:
    name = "北野善聖"
elif num == 17:
    name = "清原美瑠"
elif num == 18:
    name = "河田珂音"
elif num == 19:
    name = "河野杏奈"

print(name)
