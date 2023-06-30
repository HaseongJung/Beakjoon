n_hour, n_min, n_sec = map(int, input().split())
cook_time = int(input())

f_sec = n_sec + cook_time
f_min = (n_min + (f_sec // 60))
f_hour = n_hour + (f_min // 60)

if f_hour >= 24:
    f_hour = f_hour % 24
if f_min >= 60:
    f_min = f_min % 60
if f_sec >= 60:
    f_sec = f_sec % 60

print(f_hour, f_min, f_sec)