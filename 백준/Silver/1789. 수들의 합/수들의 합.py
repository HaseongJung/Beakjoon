S = int(input())

left, right = 1, S

N = 0

while (left <= right):
    mid = (left + right) // 2
    sum = mid * (mid+1) // 2
    if sum <= S:
        N = mid
        left = mid + 1
    else:
        right = mid - 1

print(N)