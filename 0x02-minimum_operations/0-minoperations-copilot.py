#!/usr/bin/python3
"""
Minimum operations
"""
import math

def minOperations(n):
  """
  Calculates the minimum number of operations needed to reach n H characters in a text file.

  Args:
    n: The desired number of H characters.

  Returns:
    The minimum number of operations needed, or 0 if impossible.
  """
  # Base case: 1H requires 0 operations.
  if n == 1:
    return 0

  # Initialize a dictionary to store the minimum operations needed for each number of characters.
  dp = {1: 0}

  # Iterate through possible numbers of characters (2 to n).
  for i in range(2, n + 1):
    # Calculate the minimum operations for copying all and pasting once (i // 2).
    copy_all_paste = dp[i // 2] + 2

    # If i is odd, also consider pasting twice from the previous power of 2.
    paste_twice = dp[i // 2 ** int(math.log2(i))] + 3 if i % 2 else None

    # Store the minimum of the two options.
    dp[i] = min(copy_all_paste, paste_twice) if paste_twice else copy_all_paste

  # Check if the final operation is possible (n is a power of 2).
  if n & (n - 1) == 0:
    return dp[n]

  return 0

