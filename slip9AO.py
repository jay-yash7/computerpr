import heapq

class Node:
    def __init__(self, name, cost=0, is_and_node=False):
        self.name = name
        self.cost = cost
        self.is_and_node = is_and_node
        self.children = []

    def add_child(self, child, cost):
        self.children.append((child, cost))

def ao_star(start, goal):
    open_list = [(start.cost, start)]
    while open_list:
        _, current = heapq.heappop(open_list)

        if current.name == goal.name:
            return current.name  # Return goal node when found

        if current.is_and_node:
            total_cost = 0
            for child, cost in current.children:
                total_cost += cost
                heapq.heappush(open_list, (child.cost, child))
            current.cost = total_cost
        else:
            min_cost = float('inf')
            for child, cost in current.children:
                heapq.heappush(open_list, (child.cost, child))
                min_cost = min(min_cost, cost)
            current.cost = min_cost

    return None

# Example nodes and connections
start = Node('Start', 0)
A = Node('A', 2, is_and_node=True)
B = Node('B', 3, is_and_node=False)
goal = Node('Goal')

start.add_child(A, 2)
start.add_child(B, 1)
A.add_child(goal, 1)
B.add_child(goal, 2)

# Run AO* Algorithm
result = ao_star(start, goal)
print("Path found:", result)
