import sys

T = int(input())

for _ in range(T):
    cnt = 1 

    a, b, c = map(int, input().split())

    for i in range(1, a):
        for j in range(1, b):
            for k in range(1, c):
               if (i%j == j%k) and (j%k == k%i):
                     cnt += 1      


    print(cnt)
