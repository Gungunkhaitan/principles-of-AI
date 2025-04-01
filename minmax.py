from functools import reduce

def minimax(n, d, m):
    if not isinstance(n, list) or d == 0:
        return n
    f = max if m else min
    return reduce(f, [minimax(c, d-1, not m) for c in n])

tree = [[[-1, 4], [2, 6]], [[-3, -5], [0, 7]]]
print("Game score")
print(minimax(tree, 3, True)) 