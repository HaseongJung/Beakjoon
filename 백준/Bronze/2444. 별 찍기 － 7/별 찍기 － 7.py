N = int(input())

for i in range(1, N+1):
    print(" "*(N-i) + "*"*(2*i-1))
for i in reversed(range(1, N)):
    print(" "*(N-i) + "*"*(2*i-1))