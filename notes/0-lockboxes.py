from collections import deque

def canUnlockAll(boxes):
    """
    canUnlockAll: determines whether a list of boxes with each containing
    keys can be opened
    """
    print()
    print(boxes)

    n = len(boxes)
    visited = [False] * n
    visited[0] = True

    print("Initilized visited list: ", visited)
    queue = deque([0])

    print("Initilized queue: ", queue)
    while queue:
        current_box = queue.popleft()

        print("current box", current_box)
        for key in boxes[current_box]:
            if not visited[key]:
                visited[key] = True
                queue.append(key)
                print("visited list: ", visited)
                print("queue: ", queue)

    print("Final visited: ", visited)
    return all(visited)
