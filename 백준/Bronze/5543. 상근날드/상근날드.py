buger = []
drink = []

for _ in range(3):
    buger.append(int(input()))
for _ in range(2):
    drink.append(int(input()))

print(min(buger) + min(drink) - 50)
