matrix = []
maxNum = maxRow = maxCol= 0

for i in range(9):
    nums = list(map(int, input().split()))
    matrix.append(nums)
    if maxNum <= max(nums):
        maxNum = max(nums)
        maxRow = i+1
        maxCol = nums.index(max(nums)) + 1

print(maxNum)
print(maxRow, maxCol)