from collections import deque  # Importing deque for queue implementation

def bfs(graph, root):
    visited = set()  # To track visited nodes
    queue = deque([root])  # Initialize queue with root node
    visited.add(root)  # Mark root as visited

    while queue:  # Continue while queue is not empty
        vertex = queue.popleft()  # Remove from front
        print(str(vertex) + " ", end="")  # Print node

        for neighbor in graph[vertex]:  # Add unvisited neighbors to queue
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

graph = { 
    'A': ['B', 'C', 'E'], 
    'B': ['D'], 
    'C': ['F'], 
    'D': [], 
    'E': ['F'], 
    'F': [] 
}

print("Breadth First Search: ")
bfs(graph, 'A')  # Start BFS from 'A'
