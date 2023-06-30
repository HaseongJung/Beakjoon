N = int(input())
answer = 1

for i in reversed(range(1, N+1)):
    answer *= i

print(answer)