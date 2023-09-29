import math
import sys
def input():
    return sys.stdin.readline().rstrip()

N, W, H = map(int, input().split())
diagonal = math.sqrt(W**2 + H**2)

for _ in range(N):
    length = int(input())
    if (length<=W) | (length<=H) | (length<=diagonal):
        print("DA")
    else:
        print("NE")