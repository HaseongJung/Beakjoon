N = int(input())

score = list(map(int, input().split()))
new = []

for i in range(N):
    new.append(score[i] / max(score) * 100)

print(sum(new) / N)