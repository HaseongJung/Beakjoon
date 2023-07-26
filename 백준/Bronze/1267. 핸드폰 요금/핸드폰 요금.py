import math

N = int(input())

times = list(map(int, input().split()))
fee1 = 0
fee2 = 0

for time in times:
    fee1 += (int(time/30)+1) * 10
    fee2 += (int(time/60)+1) * 15

if fee1 == fee2:
    print(f'Y M {fee1}')
elif fee1 > fee2:
    print(f'M {fee2}')
else:
    print(f'Y {fee1}')
