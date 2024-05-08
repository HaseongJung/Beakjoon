T = int(input())

for _ in range(T):
    N = int(input())
    max = 0
    mName = ''

    for i in range(N):
        S, L = input().split()
        L = int(L)
        if L > max:
            max = L
            mName = S
    print(mName)