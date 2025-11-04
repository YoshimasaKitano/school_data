# リストの練習問題

### 問題1：0から20までの乱数を10個要素に持つリストを繰返し構文を使って作成する
from random import randint
nums = []
for i in range(10):
    nums.append(randint(0,20))
print(nums)



### 問題2：問題1のリストから偶数だけのリストを作る
num2 = []
nums_copy = nums.copy()
for i in range(len(nums_copy)):
    num = nums_copy.pop()
    if num % 2 ==  0 and num > 0:
        num2.append(num)
print(num2)



### 問題3：問題1のリストの要素の合計値、最大値、最小値、平均値の計算
print(f"合計値:{sum(nums)}")
print(f"最大値:{max(nums)}")
print(f"最小値:{min(nums)}")
average_num = sum(nums) / len(nums)
print(f"平均値:{average_num}")


### 問題4：問題1のリストの並び替え（昇順）
print(sorted(nums))



### 問題5：問題1のリストの最初の要素と最後の要素の合計値を表示
nums_total = nums[0] + nums[len(nums) - 1]
print(nums_total)



