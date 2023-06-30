N, M = map(int, input().split())

a, b = [], []

for i in [a, b]:
    for j in range(N):
        i.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        a[i][j] += b[i][j]
    print(*a[i])