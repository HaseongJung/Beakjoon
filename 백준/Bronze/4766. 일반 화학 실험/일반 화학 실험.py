import sys
def input():
    return sys.stdin.readline().rstrip()

temps = []
before = 0

while (True):
    temps.append(float(input()))

    if temps[-1] == 999:
        break

    if len(temps) > 1:
        print(f'{(temps[-1] - temps[-2]):.2f}')



