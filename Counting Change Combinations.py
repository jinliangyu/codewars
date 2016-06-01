# Counting Change Combinations
"""
Description:

Write a function that counts how many different ways you can make change for
an amount of money, given an array of coin denominations. For example, there
are 3 ways to give change for 4 if you have coins with denomination 1 and 2:

1+1+1+1, 1+1+2, 2+2.
The order of coins does not matter:

1+1+2 == 2+1+1
Also, assume that you have an infinite ammount of coins.

Your function should take an amount to change and an array of unique
denominations for the coins:

  count_change(4, [1,2]) # => 3
  count_change(10, [5,2,3]) # => 4
  count_change(11, [5,7]) # => 0
"""

# my method
"""
def count_change(money, coins):
    comb = []
    combinations = []
    count_denoms(coins, comb, money, combinations)
    return len(combinations)


def count_denoms(denoms, comb, amount, combinations):
    # global combinations
    for i in range(len(denoms)):
        comb_new = comb + [denoms[i]]
        if sum(comb_new) < amount:
            count_denoms(denoms[i:], comb_new, amount, combinations)
        elif sum(comb_new) == amount:
            # print(comb_new)
            combinations.append(comb_new)
"""

# clever method 1
"""
def count_change(money, coins):
    if money<0:
        return 0
    if money == 0:
        return 1
    if money>0 and not coins:
        return 0
    return count_change(money-coins[-1],coins) + count_change(money,coins[:-1])
"""

# clever method 2
"""
def count_change(money, coins):
    dp = [1]+[0]*money
    for coin in coins:
        for x in xrange(coin,money+1):
            dp[x] += dp[x-coin]
    return dp[money]
"""
