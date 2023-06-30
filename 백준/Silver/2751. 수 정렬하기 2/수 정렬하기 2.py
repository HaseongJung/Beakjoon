import sys

N = int(sys.stdin.readline())
n = []

for _ in range(N):
    n.append(int(sys.stdin.readline()))
n = sorted(n)
for i in n:
    print(i)
