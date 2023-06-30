for _ in range(3):
    num =  list(map(int, input().split()))
    
    if num.count(0) == 1:
        print('A')
    elif num.count(0) == 2:
        print('B')
    elif num.count(0) == 3:
        print('C')
    elif num.count(0) == 4:
        print('D')
    else:
        print('E')