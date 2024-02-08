#!/usr/bin/python3
"""
Island Permiter
"""


def island_perimeter(grid):
    """Calculates the perimeter of the island provided in grid"""
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    perimeter = 0
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i + 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j + 1] == 1:
                    perimeter -= 2
#            print(grid[i][j], end=' ')
#        print()
    return perimeter


if __name__ == '__main__':
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    grid2 = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid), end='\n')
    print(island_perimeter(grid2), end='\n')
