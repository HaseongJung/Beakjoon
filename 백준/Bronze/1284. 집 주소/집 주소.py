import sys

def calWidth(nums):
    width = len(nums) + 1

    for num in nums:
        if num == 1:
            width += 2
        elif num == 0:
            width += 4
        else:
            width += 3

    return width



while(True):
    num = sys.stdin.readline().strip()
    if num == '0':
        break
    
    nums = list(map(int, num))

    answer = calWidth(nums)
    
    print(answer)