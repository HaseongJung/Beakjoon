import sys
def input():
    return sys.stdin.readline().rstrip()

answer = 0
for _ in range(10):
    lead = int(input())
    if lead == 1:
        answer += 90
    elif lead == 2:
        answer += 180
    elif lead == 3:
        answer -= 90

answer = answer % 360

if answer == 0:
    print('N')
elif answer == 90:
    print('E')
elif answer == 180:
    print('S')
elif answer == 270:
    print('W')
else:
    print(f"error, answer={answer}")