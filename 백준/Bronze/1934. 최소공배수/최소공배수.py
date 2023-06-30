T = int(input())
for i in range(T):
    a, b = map(int, input().split())
    A, B =a, b
    while a != 0:
        b = b % a
        a,b = b,a

    gcd = b
    lcm = A * B // b
    print(lcm)