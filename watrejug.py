from collections import deque

CAPACITY_A, CAPACITY_B, GOAL = 4, 3, 2

def bfs():
    queue = deque([((0, 0), [])])
    visited = set()

    while queue:
        (a, b), path = queue.popleft()
        if (a, b) in visited:
            continue
        visited.add((a, b))

        if GOAL in (a, b):
            return path + [(a, b)]

        queue.extend((state, path + [(a, b)]) 
                     for state in {(CAPACITY_A, b), (a, CAPACITY_B), (0, b), (a, 0), 
                                  (a - min(a, CAPACITY_B - b), b + min(a, CAPACITY_B - b)), 
                                  (a + min(b, CAPACITY_A - a), b - min(b, CAPACITY_A - a))} 
                     if state not in visited)

    return None

print("Solution Path:", bfs() or "No solution found.")