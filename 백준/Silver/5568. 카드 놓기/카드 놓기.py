import itertools

n = int(input())
k = int(input())
nums = []

for i in range(n):
    nums.append((input()))

new_list = []
for i in list(itertools.permutations(nums, k)):
    new_list.append(''.join(i))

new_list = set(new_list)
print(len(new_list))