from itertools import permutations

def tsp(graph, start):
    nodes = list(graph.keys())
    nodes.remove(start)
    min_cost = float('inf')
    best_path = []

    for perm in permutations(nodes):
        path = [start] + list(perm) + [start]  # Complete cycle
        cost = sum(graph[path[i]][path[i + 1]] for i in range(len(path) - 1))

        if cost < min_cost:
            min_cost = cost
            best_path = path

    return best_path, min_cost

# Example graph (Adjacency matrix representation)
graph = {
    'A': {'A': 0, 'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'B': 0, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'C': 0, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30, 'D': 0}
}

# Running TSP with 'A' as the starting point
path, cost = tsp(graph, 'A')
print("Optimal Path:", path)
print("Minimum Cost:", cost)
