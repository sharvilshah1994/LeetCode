def possibleSums(coins, quantity):
    seen = {0}
    for coin, qty in zip(coins, quantity):
        seen = {amt + part for amt in seen for part in range(0, coin * qty + 1, coin)}
    return len(seen) - 1

print(possibleSums([10, 50, 100], [1, 2, 1]))

