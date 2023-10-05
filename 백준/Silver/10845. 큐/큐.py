import sys
def input():
    return sys.stdin.readline().rstrip()

queue = []
n = int(input())
for _ in range(n):
    prompt = input().split()
    if prompt[0] == "push":
        queue.append(int(prompt[1]))
    elif prompt[0] == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
            del queue[0]
    elif prompt[0] == "size":
        print(len(queue))
    elif prompt[0] == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif prompt[0] == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif prompt[0] == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])