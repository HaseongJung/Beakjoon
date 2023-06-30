a, b, c = map(int,input().split())

n = [a, b, c]
n.sort(reverse=False)
for i in n:
    print(i, end=' ')
