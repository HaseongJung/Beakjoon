import math
import sys
def input():
    return sys.stdin.readline().rstrip()

a, b = map(int, input().split())
if a > b:
    print(b*2+1)
else:
    print(a*2-1)