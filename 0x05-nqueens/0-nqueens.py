#!/usr/bin/python3
"""
N-Queens problem solution using backtracking
"""
import sys


def print_solution(board):
    """
    Print the solution in the specified format
    """
    result = [[row, col] for row in range(len(board))
              for col in range(len(board[row])) if board[row][col] == 1]
    print(result)


def is_safe(row, col, cols, pos_diag, neg_diag):
    """
    Check if placing a queen in the current position is safe
    """
    return col not in cols and (row + col)\
        not in pos_diag and (row - col) not in neg_diag


def backtrack(row, n, cols, pos_diag, neg_diag, board):
    """
    Backtrack function to find solutions
    """
    if row == n:
        print_solution(board)
        return

    for col in range(n):
        if is_safe(row, col, cols, pos_diag, neg_diag):
            cols.add(col)
            pos_diag.add(row + col)
            neg_diag.add(row - col)
            board[row][col] = 1

            backtrack(row + 1, n, cols, pos_diag, neg_diag, board)

            cols.remove(col)
            pos_diag.remove(row + col)
            neg_diag.remove(row - col)
            board[row][col] = 0


def nqueens(board_size):
    """
    Solution to N-Queens problem
    Args:
        board_size (int): Size of the chessboard (number of queens)
    """
    cols = set()
    pos_diag = set()
    neg_diag = set()
    board = [[0] * board_size for _ in range(board_size)]

    backtrack(0, board_size, cols, pos_diag, neg_diag, board)


if __name__ == "__main__":
    args = sys.argv
    if len(args) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        board_size = int(args[1])
        if board_size < 4:
            print("N must be at least 4")
            sys.exit(1)
        nqueens(board_size)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
