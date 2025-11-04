# not call3.py
"""練習
1~30まで数えて3の倍数と3の付く値の場合だけ"Yes"で表示する
"""
count = 1

while count <= 30:

    if count % 3 == 0:
        print("yes")
        count += 1
        continue

    # if "3" in str(count):
    #     print("yes")
    #     count += 1
    #     continue
    
    if str(count).find("3") != -1:
        print("yes")
        count += 1
        continue

    print(count)
    count += 1