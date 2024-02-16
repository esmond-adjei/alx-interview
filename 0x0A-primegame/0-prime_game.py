#!/usr/bin/python3
""" Prime Game """

def is_prime(n):
  """ 
  Return prime number. Optimizes checking up to the square root of n.
  """
  if n <= 1:
    return False
  if n <= 3:
    return True
  if n % 2 == 0 or n % 3 == 0: # Optimizes by pre-checking divisibility by 2 and 3
    return False
  for i in range(5, int(n**0.5) + 1, 6):  # Iterate in steps of 6 for speed-up
    if n % i == 0 or n % (i + 2) == 0:
      return False
  return True

def delete_numbers(n, nums):
  """ 
  Remove numbers - return zero
  No longer needs a 'for' loop, optimizing iteration 
  """
  nums[:] = [num for num in nums if num % n != 0] 

def isWinner(x, nums):
  """ Return name of player that won most rounds """
  winner = False
  maria_wins = 0
  ben_wins = 0

  for _ in range(x):
    remaining_nums = list(range(1, nums[_] + 1))
    player = "Maria"

    while remaining_nums:
      for i, num in enumerate(remaining_nums):
        if is_prime(num):
          delete_numbers(num, remaining_nums)
          break
      else: 
        if player == "Maria":
          ben_wins += 1
        else:
          maria_wins += 1
        break  # Exit game loop 
      
      player = "Ben" if player == "Maria" else "Maria" # Toggle the player

  if maria_wins > ben_wins:
    return "Maria"
  elif ben_wins > maria_wins:
    return "Ben"
  else:
    return None
