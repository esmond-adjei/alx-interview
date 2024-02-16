#!/usr/bin/python3
"""
prime game
"""

def isWinner(x, nums):
    """
    Evaluates the winner of a prime game session within x rounds of play
    """
    if x < 1 or not nums:
        return None
    
    def is_prime(num):
        """Check if a number is prime."""
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    marias_wins = sum(1 for n in nums if is_prime(n))

    if marias_wins == x // 2:
        return None

    return 'Maria' if marias_wins > x // 2 else 'Ben'
