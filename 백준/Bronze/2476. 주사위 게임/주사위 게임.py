N = int(input())
price = 0

for i in range (N):
    P1, P2, P3 = map(int, input().split())

    if P1 == P2 == P3:
        price = max(price, 10000 + P1 * 1000)
    elif P1 == P2:
        price = max(price, 1000 + P1 * 100)
    elif P1 == P3:
        price = max(price, 1000 + P1 * 100)
    elif P2 == P3:
        price = max(price, 1000 + P2 * 100)
    else:
        price = max(price, max(P1, P2, P3) * 100)

print(price)