coins = [500, 100, 50, 10, 5, 1]
count = 0

cost = int(input())
change = 1000 - cost

for coin in coins:
    if change >= coin:
        if change % coin == 0:
            count += int(change / coin)
            change -= (coin * int(change / coin))       
        else:
            count += int(change / coin)
            change -= (coin * int(change / coin))
    else:
        continue

print(count)

