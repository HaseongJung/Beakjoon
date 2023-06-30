case = int(input())

for _ in range(case):
    mars = list(map(str, input().split()))
    answer = 0
    for i in range(len(mars)):
        if i == 0:
            answer += float(mars[i])
        else:
            if mars[i] == "#":
                answer -= 7
            elif mars[i] == "%":
                answer += 5
            elif mars[i] == "@":
                answer *= 3
    print(format(answer, ".2f"))