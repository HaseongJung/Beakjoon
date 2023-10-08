import sys
def input():
    return sys.stdin.readline().rstrip()

nums = sorted(list(map(int, input().split())))
chars = list(input())


for char in chars:
    if char == 'A':
        print(nums[0], end=' ')
    elif char == 'B':
        print(nums[1], end=' ')
    elif char == 'C':
        print(nums[2], end=' ')
