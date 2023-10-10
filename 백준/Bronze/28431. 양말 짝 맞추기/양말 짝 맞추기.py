import sys
def input():
    return sys.stdin.readline().rstrip()

dict = {}
for _ in range(5):
    n = int(input())
    if dict.get(n) == None:
        dict[n] = 1
    else:
        dict[n] += 1

for k, v in dict.items():
    if v%2 == 1:
        print(k)


