T = int(input())

for _ in range(T):
    R, S = map(str, input().split())
    R = int(R)
    S = list(S)
    P = ""
    
    for i in S:
        P += R * i
    print(P)