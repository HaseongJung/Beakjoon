A, B = input().split()

A = reversed(A)
B = reversed(B)
A = int(''.join(A))
B = int(''.join(B))

if A > B:
    print(A)
else:
    print(B)