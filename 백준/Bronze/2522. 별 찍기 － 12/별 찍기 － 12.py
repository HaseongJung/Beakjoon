N = int(input())

for i in range(1, N+1):
    print(' '*(N-i) + '*'*i)
for i in reversed(range(1, N)):
    print(' '*(N-i) + '*'*i)