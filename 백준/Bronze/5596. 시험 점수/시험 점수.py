Man = Min = 0
cnt = 1
for _ in range(2):
    info, math, science, eng = map(int, input().split())
    if cnt == 2:
        Min += info + math + science + eng
    else:
        Man += info + math + science + eng
    cnt += 1

if Man > Min:
    print(Man)
else:
    print(Min)
    
