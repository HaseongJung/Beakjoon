arr = sorted(list(map(int, input().split())))
width = arr[-2]
height = min(arr)

print(width*height)