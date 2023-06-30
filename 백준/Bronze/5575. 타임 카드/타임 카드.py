
for _ in range(3):
    Ah, Am, As, Lh, Lm, Ls = map(int, input().split())

    H = Lh - Ah
    M = Lm - Am
    S = Ls - As

    if M < 0:
        H -= 1
        M += 60
    if S < 0:
        M -= 1
        S += 60
        if M < 0:
            H -= 1
            M += 60
    print(H, M, S)
