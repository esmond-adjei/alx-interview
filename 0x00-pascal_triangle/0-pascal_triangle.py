#!/usr/bin/python3
"""
0-pascal-triangle
"""


def pascal_triangle(n):
    """returns a list of lists of integers representing pasacal's triangle"""
    if n <= 0:
        return []

    trgnl = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            num = trgnl[i - 1][j - 1] + trgnl[i - 1][j]
            row.append(num)
        row.append(1)
        trgnl.append(row)
    return trgnl


if __name__ == '__main__':
    print(pascal_triangle(int(input('number: '))))
