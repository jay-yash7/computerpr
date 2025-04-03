from collections import deque

# Function to perform BFS traversal
def bfs(graph, start_node):
    visited = set()  # Set to keep track of visited nodes
    queue = deque([start_node])  # Initialize queue with the start node
    
    print("BFS Traversal:", end=" ")

    while queue:
        node = queue.popleft()  # Dequeue a node
        
        if node not in visited:
            print(node, end=" ")  # Process the node
            visited.add(node)  # Mark node as visited

            # Add all unvisited adjacent nodes to the queue
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    queue.append(neighbor)

# Graph represented as an adjacency list
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

# Starting BFS from node 'A'
bfs(graph, 'A')
