T = int(input())

for _ in range(T):
    S = int(input())
    N = int(input())
    sum_option = 0
    total = 0

    for _ in range(N):
        Q, P = map(int, input().split())
        sum_option += Q * P
    total = S + sum_option
    print(total)