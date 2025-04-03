from collections import deque

def water_jug(jug1, jug2, target):
    visited = set()
    queue = deque([(0, 0)])  # Initial state (0,0)

    while queue:
        x, y = queue.popleft()

        if (x, y) in visited:
            continue
        visited.add((x, y))

        print(f"({x}, {y})")  # Print the current state

        if x == target or y == target:
            return f"Target {target} reached!"

        queue.extend([
            (jug1, y),  # Fill jug1
            (x, jug2),  # Fill jug2
            (0, y),  # Empty jug1
            (x, 0),  # Empty jug2
            (x - min(x, jug2 - y), y + min(x, jug2 - y)),  # Pour jug1 -> jug2
            (x + min(y, jug1 - x), y - min(y, jug1 - x))   # Pour jug2 -> jug1
        ])
    
    return "No solution"

# Example: 4L & 3L jugs, target = 2L
print(water_jug(4, 3, 2))
