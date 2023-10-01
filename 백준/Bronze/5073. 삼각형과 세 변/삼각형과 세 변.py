import sys
def input():
    return sys.stdin.readline().rstrip()

while (True):
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break
    elif sum([a, b, c]) - max([a, b, c]) <= max([a, b, c]):
        print("Invalid")
    elif (a == b == c):
        print("Equilateral")
    elif (a==b) | (b==c) | (c==a):
        print("Isosceles")
    else:
        print("Scalene")
