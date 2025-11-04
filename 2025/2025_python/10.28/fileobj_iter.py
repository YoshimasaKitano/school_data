### fileobj_iter.py
"""
ファイルオブジェクトをイテレータとして扱う
"""
file = "./10.28/read_file_sample.py"

target = "text"

with open(file, "r", encoding = "utf-8") as fileobj:
    while True:
        try:
            line = next(fileobj)

            if line.find(target) >= 0:
                print(f"「{target}」が見つかりました。") 
                print(line, end = "")
                break
        except StopIteration:
            print(f"「{target}」が見つかりませんでした。")
            break