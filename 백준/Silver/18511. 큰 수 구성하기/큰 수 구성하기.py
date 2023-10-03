import sys
from itertools import product
def input():
    return sys.stdin.readline().rstrip()

n, k = map(int,input().split())
arr = input().split()
length = len(str(n))
nums = []

while True:
    for num in list((product(arr, repeat=length))):
        tmp = int(''.join(num))
        if tmp <= n:
            nums.append(tmp)
    if len(nums) >= 1:
        print(max(nums))
        break
    else:
        length -= 1

