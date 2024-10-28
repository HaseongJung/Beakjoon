def fibo(n: int):
    arr = []
    for i in range(n):
        if (i <= 1):
            arr.append(i)
        else:
            arr.append(arr[i-2] + arr[i-1])

    return arr


if __name__ == "__main__":
    n = int(input())
    print(fibo(n+1)[-1])