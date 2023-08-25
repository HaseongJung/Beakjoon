import sys

nums = [0, 1]
n = int(sys.stdin.readline())

for i in range(2, n+1):
    nums.append(sum(nums[-2:]))

print(nums[n])