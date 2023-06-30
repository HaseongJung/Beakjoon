M = int(input())
N = int(input())
sosu = []

for i in range(M, N+1):
    if i > 1:
        count = 0
        for x in range(1, i+1):
            if i % x == 0:
                count += 1
        if count == 2:
            sosu.append(i)

if sosu == []:
    print(-1)
else:
    print(sum(sosu))
    print(sosu[0])