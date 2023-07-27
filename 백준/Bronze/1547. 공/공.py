import sys

M = int(input())
cups = [1, 0, 0]

for _ in range(M):
    num1, num2 = map(int, sys.stdin.readline().split())
    cups[num1-1], cups[num2-1] = cups[num2-1], cups[num1-1]

for cup in cups:
    if cup == 1:
        print(cups.index(cup)+1)
