import heapq

def beam_search(graph, start, goal, k):
    queue = [(0, [start])]
    while queue:
        queue = sorted(queue)[:k]
        new_queue = []
        for cost, path in queue:
            if path[-1] == goal:
                return path
            for neighbor, weight in graph[path[-1]].items():
                if neighbor not in path:
                    heapq.heappush(new_queue, (cost + weight, path + [neighbor]))
        queue = new_queue
    return None

graph={1:{2:3,3:2,4:10},2:{3:1,4:2},3:{4:1,1:5},4:{}}
print("Path:", beam_search(graph, 1, 4, 2))