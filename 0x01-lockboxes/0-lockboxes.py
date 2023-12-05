from collections import deque


def canUnlockAll(boxes):
    """
    canUnlockAll: determines whether a list of boxes with each containing
    keys can be opened
    """
    n = len(boxes)
    visited = [False] * n
    visited[0] = True

    queue = deque([0])

    while queue:
        current_box = queue.popleft()

        for key in boxes[current_box]:
            if not visited[key]:
                visited[key] = True
                queue.append(key)

    return all(visited)
