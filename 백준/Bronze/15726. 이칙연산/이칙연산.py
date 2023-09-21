A, B, C = map(int, input().split())
answer = 0

if B > C:
    answer = int(A*B/C)
else:
    answer = int(A/B*C)


print(answer)
