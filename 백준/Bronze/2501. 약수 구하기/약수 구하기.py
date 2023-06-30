N, K = map(int, input().split())
measure = []

for x in range(1, N+1):
    if N % x == 0:
        measure.append(x)


if K > len(measure):
    print(0)
else:
    print(measure[K-1])