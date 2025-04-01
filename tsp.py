import random

def tsp_hill_climbing(graph):
    n = len(graph)
    path = list(range(n))
    random.shuffle(path)
    def cost(p): return sum(graph[p[i]][p[i+1]] for i in range(n-1)) + graph[p[-1]][p[0]]
    
    while True:
        neighbors = [path[:i] + path[i:j+1][::-1] + path[j+1:] for i in range(n) for j in range(i+1, n)]
        best_neighbor = min(neighbors, key=cost)
        if cost(best_neighbor) >= cost(path):
            break
        path = best_neighbor
    return path, cost(path)

graph = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
path, min_cost = tsp_hill_climbing(graph)
print("Optimal Path:", path, "\nMinimum Cost:", min_cost)