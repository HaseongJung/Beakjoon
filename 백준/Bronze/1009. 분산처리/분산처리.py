import sys
def input():
    return sys.stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    
    #answer = a**(b%10) % 10
    #if answer == 0:
    #    print(10)

    a = a % 10
    if a == 0:
        print(10)
    elif (a==1) | (a==5) | (a==6):
        print(a)
    elif (a==4) | (a==9):
        b = b % 2
        if b == 1:
            print(a)
        else:
            print((a*a) % 10) 
    else:
        b = b % 4
        if b == 0:
            print((a**4) % 10)
        else:
            print((a**b) % 10)