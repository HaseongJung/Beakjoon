case = int(input())

for i in range(case):
    ox_lsit = list(input())
    score = 0
    sum_score = 0
    for ox in ox_lsit:
        if ox == 'O':
            score += 1
            sum_score += score
        else:
            score = 0
    print(sum_score)
