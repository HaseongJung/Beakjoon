num = [] 
odd = []

for _ in range(7):
    number = int(input())
    num.append(number)

for i in num:
    if i % 2 == 1:
        odd.append(i)

if odd == []:
    print(-1)
else:    
    print(sum(odd))
    print(min(odd))