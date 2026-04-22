def split_money(amount, coins, current=[]):
    if amount == 0:
        print(current)
        return
    if amount < 0:
        return

    for i in range(len(coins)):
        split_money(amount - coins[i], coins[i:], current + [coins[i]])
coins = [1, 2, 5]
split_money(5, coins)