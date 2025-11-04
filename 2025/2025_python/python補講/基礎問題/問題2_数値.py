## 数値に関する問題（10問）
### 低レベル（3問）
# Q1：numA、numB、numC、numD、numEの５つの変数にそれぞれ2,3,5,7,11を代入し、文字列連結を使って表示
""" 実行結果表示例
numA:2
numB:3
numC:5
numD:7
numE:11
"""
numA = 2
numB = 3
numC = 5
numD = 7
numE = 11
print("numA:" + str(numA))
print("numB:" + str(numB))
print("numC:" + str(numC))
print("numD:" + str(numD))
print("numE:" + str(numE))
print()



# Q2：numA、numB、numC、numD、numEの5つの整数の合計を表示
""" 実行結果表示例
numA、numB、numC、numD、numEの5つの整数の合計: 28
"""
print(f"numA、numB、numC、numD、numEの5つの整数の合計:  + {str(numA + numB + numC + numD + numE)}")
print()


# Q3：numDを3倍して表示
""" 実行結果表示例
numDを3倍: 21
"""
print(f"numDを3倍: {str(numD * 3)}")
print()


### 中レベル（4問）
# Q4：numCとnumDの2つの整数の差の絶対値を表示（平方根を利用）
""" 実行結果表示例
numCとnumDの2つの整数の差の絶対値: 2.0
"""
ans = abs(float(numC - numD))
print(f"numCとnumDの2つの整数の差の絶対値: {ans}")
print()


# Q5：半径numBから円の面積を求める（π=3.14）
""" 実行結果表示例
半径numBから円の面積: 78.5
"""
π = 3.14
circle = (numC ** 2) * π
print(f"半径numBから円の面積: {circle}")
print()


# Q6：整数numBを浮動小数型に変換して1.5倍した値を表示
""" 実行結果表示例
整数numBを浮動小数型に変換して1.25倍した値: 6.25
"""
ans = float(numC * 1.25)
print(f"整数numCを浮動小数型に変換して1.25倍した値: {ans}")
print()


# Q7：numA、numB、numC、3つの整数の平均を小数点第2位まででまるめ処理して表示
""" 実行結果表示例
numA、numB、numC、3つの整数の平均: 3.33
"""
ans = round((numA + numB + numC) / 3, 2)
print(ans)
print()



### 高レベル（3問）
# Q8：numAとnumBの和をnumCで割った商と余りを表示
""" 実行結果表示例
numAとnumBの和をnumCで割った商: 1
numAとnumBの和をnumCで割った余り: 0
"""
ans1 = (numA + numB) / numC
ans2 = (numA + numB) % numC
print(f"numAとnumBの和をnumCで割った商: {int(ans1)}")
print(f"numAとnumBの和をnumCで割った余り: {ans2}")
print()



# Q9：任意の価格と小数点以下を切り捨てした税込価格（税率10%）を表示
""" 実行結果表示例
価格を入力→100
100円の10%税込価格:110円
"""
price = int(input("価格を入力→"))
ans = (price * 0.1) + price
print(f"{price}円の10%税込価格:{int(ans)}円")
print()



# Q10：任意の金額を入力、500円硬貨から1円硬貨まで順に枚数を表示
""" 実行結果表示例
金額を入力→12345
500円硬貨:24円
100円硬貨:3円
50円硬貨:0円
10円硬貨:4円
5円硬貨:1円
1円硬貨:0円
"""
money = int(input("金額を入力→"))
en500 = money // 500
money %= 500
en100 = money // 100
money %= 100
en50 = money // 50
money %= 50
en10 = money // 10
money %= 10
en5 = money // 5
money %= 5
en1 = money // 1
print(f"500円硬貨:{en500}枚")
print(f"100円硬貨:{en100}枚")
print(f"50円硬貨:{en50}枚")
print(f"10円硬貨:{en10}枚")
print(f"5円硬貨:{en5}枚")
print(f"1円硬貨:{en1}枚")






