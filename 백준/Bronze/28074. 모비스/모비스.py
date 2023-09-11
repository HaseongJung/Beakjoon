def inMOBIS(word):
    mobis = list("MOBIS")

    flag = True
    for char in mobis:
        if char not in word:
            flag = False
    return flag

def main():
    word = list(input())

    if inMOBIS(word):
        print("YES")
    else:
        print("NO")

main()