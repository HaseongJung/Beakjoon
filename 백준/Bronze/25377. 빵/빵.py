answer = 0

N = int(input())

for _ in range(N):
    A, B = map(int, input().split())
    
    if A <= B:
        if answer == 0:
            answer = B
        else:
            answer = min(answer, B)

if answer == 0:
    print(-1)
else:
    print(answer)