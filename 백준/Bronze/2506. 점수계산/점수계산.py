N = int(input())
result = list(map(int, input().split()))
score = 1
totalscore = 0

for  i in range(N):
    if result[i] == 1:
        totalscore += score
        score += 1
    elif result[i] == 0:
        score = 1
        
print(totalscore)