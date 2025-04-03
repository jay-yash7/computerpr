import heapq

def a_star(graph, start, goal, heuristic):
    open_list = [(0 + heuristic[start], 0, start, [])]  # (f, g, node, path)
    visited = set()

    while open_list:
        f, g, node, path = heapq.heappop(open_list)

        if node in visited:
            continue
        visited.add(node)

        path = path + [node]
        if node == goal:
            return path

        for neighbor, cost in graph[node].items():
            if neighbor not in visited:
                heapq.heappush(open_list, (g + cost + heuristic[neighbor], g + cost, neighbor, path))

    return None

# Example graph (Adjacency list)
graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'A': 1, 'D': 3, 'E': 2},
    'C': {'A': 3, 'E': 1},
    'D': {'B': 3, 'E': 1},
    'E': {'B': 2, 'C': 1, 'D': 1}
}

# Heuristic values (from node to goal 'E')
heuristic = {'A': 4, 'B': 3, 'C': 2, 'D': 1, 'E': 0}

# Running A* algorithm
path = a_star(graph, 'A', 'E', heuristic)
print("Path from A to E:", path)
