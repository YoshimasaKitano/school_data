### fileobj_iter_for.py
"""
ファイルオブジェクトをイテレータとして扱う
"""
file = "./10.28/read_file_sample.py"

target = "text"

with open(file, "r", encoding = "utf-8") as fileobj:
    for line in fileobj:
        # if line.find(target) >= 0:
        #     print(f"「{target}」が見つかりました。") 
        #     print(line, end="")
        #     break
        if target in line:
            print(f"「{target}」が見つかりました。") 
            print(line, end="")
            break
    else:
        print(f"「{target}」が見つかりまんでした。")