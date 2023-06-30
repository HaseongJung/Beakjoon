word = input()
answer = []

for i in word:
    if i.isupper() == True:
        answer.append(i.lower())
    elif i.islower() == True:
        answer.append(i.upper())

print(''.join(answer))