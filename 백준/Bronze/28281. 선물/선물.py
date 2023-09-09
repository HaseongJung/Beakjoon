N, X = map(int, input().split())
prices = list(map( int, input().split()))
total = 99999999999999999999999999999


def calExpense(day1, day2):
    global prices
    expense = 0
    expense += prices[day1] * X + prices[day2] * X
    return expense

for i in range(len(prices)-1):
    price = calExpense(i , i+1)
    if total > price:
        total = price

print(total)