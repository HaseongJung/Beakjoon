while(True):
    word = input()
    if word == '0':
        break
    elif word == word[::-1]:
        print("yes")
    else:
        print("no")
       