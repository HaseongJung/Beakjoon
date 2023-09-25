import sys
def input():
    return sys.stdin.readline().rstrip()

price = 0
max_total = 0

for i in range(5):
    scores = list(map(int, input().split()))
    total = sum(scores)
    if total > max_total:
        max_total = total
        price = i+1

print(price, max_total)