import sys
def input():
    return sys.stdin.readline().rstrip()

cnt = 0

while (True):
    line = input()
    if line == '':
        break
    cnt += 1

print(cnt)