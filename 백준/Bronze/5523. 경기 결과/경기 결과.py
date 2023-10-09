import sys
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
aScore = bScore = 0
for _ in range(n):
    a, b = map(int, input().split())
    if a > b:
        aScore += 1
    elif a < b:
        bScore += 1

print(aScore, bScore)


