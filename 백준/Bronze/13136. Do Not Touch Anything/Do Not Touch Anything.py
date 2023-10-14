import math
import sys
def input():
    return sys.stdin.readline().rstrip()

r, c, n = map(int, input().split())

x = math.ceil(r/n)
y = math.ceil(c/n)

print(x*y)