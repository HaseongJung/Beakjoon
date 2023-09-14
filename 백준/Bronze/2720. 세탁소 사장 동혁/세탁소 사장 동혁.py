import sys

T = int(input())

for _ in range(T):
    C = int(sys.stdin.readline())
    
    for i in [25, 10, 5, 1]:
        print(C // i, end=' ')
        C = C % i