while (True):
    name, age, weight = input().split()
    age, weight = int(age), int(weight)

    if name=='#' and age==0 and weight==0:
        break

    elif age>17 or weight>=80:
        print(name, "Senior")
    else:
        print(name, "Junior")