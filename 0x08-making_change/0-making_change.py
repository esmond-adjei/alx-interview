#!/usr/bin/python3
"""
Change comes from within :)
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values,
    determine the fewest number of coins needed to meet
    a given amount in total.
    """
    if total <= 0:
        return 0
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            # print(f"dp[i] -> {dp[i]}, dp[{i} - {coin}] -> {dp[i - coin]}")
            dp[i] = min(dp[i], dp[i - coin] + 1)
            # print(dp[i])

    return dp[total] if dp[total] != float('inf') else -1
