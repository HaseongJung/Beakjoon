import sys
def input():
    return sys.stdin.readline().rstrip()

def main():
    a ,b = map(int, input().split())
    c, d = map(int, input().split())
    arr = [a ,c, b, d]  # [c ,d, a, b]   # [d, b, c, a]
    
    answers = [arr[0]/arr[1] + arr[2]/arr[3]]
    for i in range(5):
        arr = [arr[1], arr[3], arr[0], arr[2]]
                
        answer = arr[0]/arr[1] + arr[2]/arr[3]
        answers.append(answer)
    print(answers.index(max(answers)))
    
if __name__ == '__main__':
    main()