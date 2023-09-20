N,M,L =  map(int,input().split())
arr = [0] + list(map(int,input().split())) + [L]

# 0 82 201 411 555 622 755 800
arr.sort()

start, end = 1, L-1
answer = 0

while start <= end:
    cnt = 0
    mid = (start+end) // 2

    for i in range(1,len(arr)):
        if arr[i] - arr[i-1] > mid:
            cnt += (arr[i] - arr[i-1]-1) // mid

    if cnt > M:
        start = mid+1
    else:
        end = mid-1
        answer = mid

print(answer)