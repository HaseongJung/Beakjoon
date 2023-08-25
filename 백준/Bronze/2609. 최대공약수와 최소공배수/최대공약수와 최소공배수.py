import sys

A, B = map(int, sys.stdin.readline().split())
a, b = max(A, B), min(A, B)

while b != 0:
    a = a % b
    a, b = b, a

print(a)
print(int(A*B//a))


