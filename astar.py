import heapq

def a_star(graph, start, goal, heuristic):
    queue = [(0, start, [])]  # (f-score, current node, path)
    visited = set()
    
    while queue:
        cost, node, path = heapq.heappop(queue)
        
        if node in visited:
            continue
        path.append(node)

        if node == goal:
            return path
        
        visited.add(node)

        for neighbor, cost in graph[node]:
            if neighbor not in visited:
                heapq.heappush(queue, (cost + heuristic[neighbor], neighbor, path[:]))  # Copy path for each branch
    
    return None

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}
heuristic = {'A': 7, 'B': 6, 'C': 2, 'D': 0}

print("A* Path:", a_star(graph, 'A', 'D', heuristic))