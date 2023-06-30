N = int(input())
star = 1

for i in range(1, N+1):
    print((((2*N-1) - star)//2) * " " + "*"*star)
    star += 2