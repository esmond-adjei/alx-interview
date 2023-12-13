#!/usr/bin/python3
"""
Minimum operations
"""

def minOperations(n):
    if n <= 1:
        return 0

    # dp[i] represents the minimum number of operations to get i 'H' characters
    dp = [float('inf')] * (n + 1)
    dp[1] = 0  # Base case

    for i in range(2, n + 1):
        for j in range(2, i + 1):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)

    return dp[n]

