import sys
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
for _ in range(n):
    stc = input()
    print(stc[0].upper() + stc[1::])