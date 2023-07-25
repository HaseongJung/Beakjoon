import sys

for _ in range(3):
    N = int(sys.stdin.readline())
    answer = 0

    for i in range(N):
        answer += int(sys.stdin.readline())
    if answer == 0:
        print(0)
    elif answer > 0:
        print('+')
    else:
        print('-')
