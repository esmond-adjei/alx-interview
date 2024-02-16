#!/usr/bin/python3
"""
Prime Game
"""


def isprime(n):
    """ Return prime number """
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def update_nums(n, nums):
    """ Remove numbers"""
    for i in range(len(nums)):
        if nums[i] % n == 0:
            nums[i] = 0


def isWinner(x, nums):
    """ Return name of player that won
    most rounds
    """
    nums.sort()
    Maria = 0
    Ben = 0
    for game in range(x):
        nums2 = list(range(1, nums[game] + 1))
        turn = 0
        while True:
            """
            # monitor turns, uncomment to watch
            if turn % 2 != 0:
                print("Ben turn ")
            else:
                print("Maria turn ")
            """
            change = False
            for i, n in enumerate(nums2):
                if n > 1 and isprime(n):
                    update_nums(n, nums2)
                    change = True
                    turn += 1
                    break
            if change is False:
                break
        if turn % 2 != 0:
            Maria += 1
        else:
            Ben += 1
    if Maria == Ben:
        return None
    if Maria > Ben:
        return "Maria"
    return "Ben"
