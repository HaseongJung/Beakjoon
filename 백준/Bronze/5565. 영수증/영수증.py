total = int(input())
sum = 0

for _ in range(9):
    price = int(input())
    sum += price

answer = total - sum
print(answer)