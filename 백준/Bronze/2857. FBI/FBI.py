import sys
def input():
    return sys.stdin.readline().rstrip()

names = []
answer = []
for i in range(5):
    name = input()
    names.append(name)
    if "FBI" in name:
        answer.append(i+1)

if len(answer) ==  0:
    print("HE GOT AWAY!")
else:
    for name in answer:
        print(name, end=' ')

