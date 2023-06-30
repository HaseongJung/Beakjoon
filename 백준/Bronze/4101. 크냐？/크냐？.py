while True:

    a, b = map(int, input().split())
    
    if a == b == 0:
        break
    elif a > b:
        print("Yes")
    else:
        print("No")
