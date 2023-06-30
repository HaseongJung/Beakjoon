num = list(map(int, input().split()))

if num == sorted(num):
    print("ascending")
elif num == sorted(num, reverse=True):
    print("descending")
else:
    print("mixed")