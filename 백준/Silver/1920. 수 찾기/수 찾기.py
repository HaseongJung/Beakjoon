N = int(input())
num_A = set(map(int, input().split()))

M = int(input())
num_B = list(map(int, input().split()))

for B in (num_B):
    if B in  num_A:
        print(1)
    else:
        print(0)