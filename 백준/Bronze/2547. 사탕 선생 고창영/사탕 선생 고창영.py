import sys
def input():
    return sys.stdin.readline().rstrip()

T =  int(input())

for _ in range(T):
    input()
    total = 0
    N = int(input())
    for _ in range(N):
        total += int(input())
        

    if total%N == 0:
        print("YES")
    else:
        print("NO")