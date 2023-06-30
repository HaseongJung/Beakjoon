n = int(input())

result = [i for i in range(n+1)]
for i in range(2, n+1):
    result[i] = result[i-1] + result[i-2]

print(result[-1])