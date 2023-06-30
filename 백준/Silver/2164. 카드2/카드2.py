import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
nlist = [i for i in range(1, N+1)]
nlist = deque(nlist)

def solution(nlist):
    while len(nlist) > 1:
        nlist.popleft()
        nlist.append(nlist.popleft())

    print(nlist[0])

solution(nlist)
