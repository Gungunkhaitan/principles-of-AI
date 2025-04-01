graph = {
    '1': ['2', '3'],
    '2': ['4', '5'],
    '3': [],
    '4': ['6'],
    '5': [],
    '6': []
}

visited = set()  # Stores visited nodes

def dfs(visited, graph, node):
    if node not in visited:
        print(node + " ", end="")  # Print visited node
        visited.add(node)  # Mark as visited
        for neighbor in graph[node]:  # Visit all neighbors recursively
            dfs(visited, graph, neighbor)

print("Depth First Search: ")
dfs(visited, graph, '1')  # Start DFS from node '1'

