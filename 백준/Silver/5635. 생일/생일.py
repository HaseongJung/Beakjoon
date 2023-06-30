n = int(input())
list =[]

for _ in range(n):
    n, d, m, y =input().split()
    list.append([n, int(d), int(m), int(y)])
list.sort(key = lambda x: (x[3], x[2], x[3]))
print(list[-1][0])
print(list[0][0])