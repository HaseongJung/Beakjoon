a, b = map(int, input().split())

if a > b:
    width = (a-1)//4 - (b-1)//4
else:
    width = (b-1)//4 - (a-1)//4

length = (a-1)%4 - (b-1)%4

if length < 0:
    answer = width - length
else:
    answer = width + length


#print(f'width={width} length={length}')
print(answer)
