#!/usr/bin/python3
"""
prime game
"""


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def remove_multiples(nums, prime):
    return [num for num in nums if num % prime != 0]


def isWinner(x, nums):
    maria_wins = 0
    ben_wins = 0
    player = "Maria"
    for _ in range(x):
        while True:
            for num in nums:
                if is_prime(num) and all(num % other != 0 for other in nums):
                    break
            else:
                if player == "Maria":
                    ben_wins += 1
                else:
                    maria_wins += 1
                break
            nums = remove_multiples(nums, num)
            player = "Ben" if player == "Maria" else "Maria"

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
