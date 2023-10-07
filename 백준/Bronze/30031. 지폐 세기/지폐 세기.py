import sys
def input():
    return sys.stdin.readline().rstrip()

total = 0
N = int(input())
for _ in range(N):
    width, height = map(int, input().split())
    if width == 136:
        total += 1000
    elif width == 142:
        total += 5000
    elif width == 148:
        total += 10000
    elif width == 154:
        total += 50000

print(total)