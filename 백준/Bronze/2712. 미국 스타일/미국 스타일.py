import sys
def input():
    return sys.stdin.readline().rstrip()

for _ in range(int(input())):
    values = input().split()
    value = float(values[0])
    if values[1] == "kg":
        print(f'{value*2.2046:.4f} lb')
    elif values[1] == "lb":
        print(f'{value*0.4536:.4f} kg')
    elif values[1] == 'l':
        print(f'{value*0.2642:.4f} g')
    elif values[1] == 'g':
        print(f'{value*3.7854:.4f} l')
