import sys
def input():
    return sys.stdin.readline().rstrip()

def main():
    T = int(input())

    for _ in range(T):
        A, B = map(int, input().split())
        print(A + B)

if __name__ == "__main__":
    main()