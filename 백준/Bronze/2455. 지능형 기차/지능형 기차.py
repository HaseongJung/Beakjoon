total = 0
people = []

for i in range(4):
    A, B = map(int, input().split())
    total = total -A + B
    people.append(total)

print(max(people))