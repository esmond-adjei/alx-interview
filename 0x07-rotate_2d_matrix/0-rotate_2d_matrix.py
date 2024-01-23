#!/usr/bin/python3
"""
Rotates 2d Matrix
"""


def rotate_2d_matrix(matrix):
    """
    Given n x n 2D matrix, rotates it by 90 degress clockwise.
    """
    dim = len(matrix[0])
    for r in range(dim):
        for c in range(dim):
            if r < c:
                # transpose
                matrix[r][c], matrix[c][r] = \
                        matrix[c][r], matrix[r][c]
            if c >= dim/2:
                # reflect
                matrix[r][c], matrix[r][dim-1-c] = \
                        matrix[r][dim-1-c], matrix[r][c]
