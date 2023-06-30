L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

cA = A/C
if A/C % 1 > 0:
    cA = int(cA) + 1
else:
    cA = int(cA)

cB = B/D
if B/D % 1 > 0:
    cB = int(cB) + 1
else:
    cB = int(cB)
    
if cA > cB:
    print(L - cA)
else:
    print(L - cB)
