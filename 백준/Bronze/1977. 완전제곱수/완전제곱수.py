M = int(input())
N = int(input())

list = []

for i in range(M, N+1):
    if (i ** (1/2)) % 1 == 0:
        list.append(i)

if list == []:
    print(-1)
else:       
    print(sum(list))
    print(list[0])