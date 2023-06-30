a = int(input())
b = int(input())
c = int(input())

answer = a * b * c
answer_list = []
for i in str(answer):
    answer_list += i

for i in range(10):
    print(answer_list.count(str(i)))