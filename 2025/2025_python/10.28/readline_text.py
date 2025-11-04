### readline_text.py
"""
ファイルからテキストを1行ずつ読み込む
"""

file = "./10.28/read_file_sample.py"
with open(file, "r", encoding = "utf-8") as fileobj:
    for line in fileobj:
        aline = line.rstrip()
        if aline:
            print(aline)
            
    # while True:
    #     line = fileobj.readline()
    #     aline = line.rstrip()

    #     if aline:
    #         print(aline)
    #     else:
    #         break