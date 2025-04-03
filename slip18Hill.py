import random

def objective_function(x):
    """Function to maximize: f(x) = - (x - 3)² + 9"""
    return - (x - 3) ** 2 + 9  # A quadratic function with max at x = 3

def hill_climbing(start_x, step_size, max_iterations):
    """Performs Hill Climbing to find the maximum of the objective function"""
    current_x = start_x
    current_value = objective_function(current_x)

    for _ in range(max_iterations):
        # Generate a new candidate solution (left or right step)
        new_x = current_x + random.choice([-step_size, step_size])
        new_value = objective_function(new_x)

        # Move to the new point if it's better
        if new_value > current_value:
            current_x = new_x
            current_value = new_value
        else:
            break  # Stop if no improvement

    return current_x, current_value

# Running the Hill Climbing algorithm
best_x, best_value = hill_climbing(start_x=random.uniform(-10, 10), step_size=0.1, max_iterations=100)
print(f"Best solution: x = {best_x}, f(x) = {best_value}")
