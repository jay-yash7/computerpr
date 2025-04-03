# Depth First Search (DFS) Algorithm

def dfs(graph, start_node, visited=None):
    """Function to perform DFS traversal"""
    if visited is None:
        visited = set()  # Set to track visited nodes

    traversal_order = []  # List to store DFS order
    stack = [start_node]  # Stack initialized with the start node

    while stack:
        node = stack.pop()  # Pop a node from the stack

        if node not in visited:
            traversal_order.append(node)  # Process the node
            visited.add(node)  # Mark as visited

            # Push all unvisited adjacent nodes in reverse order (to maintain order)
            for neighbor in reversed(graph.get(node, [])):
                if neighbor not in visited:
                    stack.append(neighbor)

    return traversal_order

# Example Graph (Adjacency List Representation)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B', 'H'],
    'F': ['C'],
    'G': ['C'],
    'H': ['E']
}

# Starting DFS from node 'A'
result = dfs(graph, 'A')
print("DFS Traversal:", result)
