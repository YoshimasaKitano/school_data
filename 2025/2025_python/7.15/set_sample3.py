# set_sample3.py
"""
セットの集合演算
和集合 | union()
積集合 & intersection()
差集合 - difference()
対称差集合 ^ symmetric_difference()
"""
a = {"みかん", "りんご", "もも", "いちご"}
b = {"すいか", "みかん", "ばなな", "もも"}

# 和集合:両方の要素を持ち合わる
f_set1 = a | b
print(f_set1) ### {'りんご', 'もも', 'ばなな', 'みかん', 'すいか', 'いちご'}

f_set1 = a.union(b)
print(f_set1) ### {'りんご', 'すいか', 'ばなな', 'いちご', 'もも', 'みかん'}

# 積集合
f_set2 = a & b
print(f_set2) ### {'みかん', 'もも'}

f_set2 = a.intersection(b)
print(f_set2) ### {'もも', 'みかん'}

# 差集合
f_set3 = a - b # aからbの要素を取り除いた残り
print(f_set3) ### {'いちご', 'りんご'}

f_set3 = a.difference(b)
print(f_set3) ### {'いちご', 'りんご'}

# 対称差集合
f_set4 = a ^ b
print(f_set4) ### {'りんご', 'ばなな', 'すいか', 'いちご'}

f_set4 = a.symmetric_difference(b)
print(f_set4) ### {'すいか', 'ばなな', 'いちご', 'りんご'}

print(f_set1 - f_set2 == f_set4) ### True

"""
集合演算の結果でアップデートする
"""
# 和集合で更新
data = {"red", "blue"}
data2 = {"blue", "yellow"}
data3 = {"blue", "green"}

data.update(data2, data3)
print(data) ### {'green', 'red', 'blue', 'yellow'}

data = {"red", "blue"}
data2 = {"blue", "yellow"}
data3 = {"blue", "green"}

## data, data2, data3の和集合でdataを更新
data = data | data2 | data3
print(data) ### {'green', 'yellow', 'red', 'blue'}


data = {"red", "blue"}
data2 = {"blue", "yellow"}
data3 = {"blue", "green"}

## data = data | data2
data |= data2
print(data) ### {'blue', 'red', 'yellow'}

## data = data | data3
data |= data3
print(data) ### {'blue', 'red', 'green', 'yellow'}

# 積集合で更新
data = {"red", "blue"}
data2 = {"blue", "yellow"}
data3 = {"blue", "green"}

data.intersection_update(data2)
print(data) ### {'blue'}

data = {"red", "blue"}
data = data & data2
print(data) ### {'blue'}

data = {"red", "blue"}
data &= data2
print(data) ### {'blue'}

# 差集合で更新
data = {"red", "blue"}
data2 = {"blue", "yellow"}
data3 = {"blue", "green"}

data.difference_update(data2)
print(data) ### {'red'}

data = {"red", "blue"}
data = data - data2
print(data) ### {'red'}

data = {"red", "blue"}
data -= data2
print(data) ### {'red'}

# 対称差集合で更新
data = {"red", "blue"}
data2 = {"blue", "yellow"}
data3 = {"blue", "green"}

data.symmetric_difference_update(data2)
print(data) ### {'yellow', 'red'}

data = {"red", "blue"}
data = data ^ data2
print(data) ### {'red', 'yellow'}

data = {"red", "blue"}
data ^= data2
print(data) ### {'yellow', 'red'}

"""
セットの比較
"""
# 比較演算子
a = {1, 2, 3}
b = {3, 2, 1}
c = {1, 2, 3, 4}
d = {6, 7, 8, 9}

## 要素が同じか？
print(a == b) ### True
print(a == c) ### False
print(a is b) ### False
print(a is c) ### False

## 要素が同じではない？
print(a != b) ### False
print(a != c) ### True

# 共通の要素がある→False/ない→True
print(a.isdisjoint(b)) ### False
print(a.isdisjoint(c)) ### False
print(a.isdisjoint(d)) ### True 共通の要素が全くない

"""
セットの包含関係
"""
Aset = {"ハンバーグ", "チキン", "ポテト", "コーン", "ウインナー"}
Bset = {"ハンバーグ", "ポテト", "コーン"}
Cset = {"エビフライ", "コーン", "ポテト"}

# AsetはBsetのサブセット(部分)か？
print(Aset.issubset(Bset)) ### False

# BsetはAsetのサブセットか？
print(Bset.issubset(Aset)) ### True

# AsetはBsetのスーパーセット(含んでいる)か？
print(Aset.issuperset(Bset)) ### True

# BsetはAsetのスーパーセット(含んでいる)か？
print(Bset.issuperset(Aset)) ### False

# AsetはCsetのスーパーセットか？
print(Aset.issuperset(Cset)) ### False