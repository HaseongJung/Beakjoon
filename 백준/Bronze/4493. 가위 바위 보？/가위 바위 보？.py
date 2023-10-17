import sys
def input(): 
    return sys.stdin.readline().rstrip()

def RSP(a, b):
    if a == 'R':
        if b == 'R':
            return 0
        elif b == 'S':
            return 1
        else:
            return -1
    elif a == 'S':
        if b == 'R':
            return -1
        elif b == 'S':
            return 0
        else:
            return 1
    elif a == 'P':
        if b == 'R':
            return 1
        elif b == 'S':
            return -1
        else:
            return 0

def main():
    for _ in range(int(input())):   # test case
        score = 0

        for _ in range(int(input())):    # game count
            a, b = input().split()
            score += RSP(a, b)

        if score > 0:
            print('Player 1')
        elif score == 0:
            print('TIE')
        else:
            print('Player 2')
        

if __name__ == '__main__':
    main()