ISBN = [9,7,8,0,9,2,1,4,1,8]

answer = 0

for _ in range(3):
    ISBN.append(int(input()))

answer += sum(ISBN[0::2])
for i in ISBN[1::2]:
    answer += i*3

print("The 1-3-sum is", answer)


