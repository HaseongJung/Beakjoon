answer = 0
current = 0

for _ in range(10):
    off, on = map(int, input().split())

    current -= off
    current += on
    
    if current > answer:
        answer = current

print(answer)