# List Operations in Python

# 1. Creating a Nested List
nested_list = [[1, 2, 3], [4, 5, 6], ["A", "B", "C"]]
print("Nested List:", nested_list)

# 2. Finding the Length of a List
length = len(nested_list)
print("Length of Nested List:", length)

# 3. List Concatenation
list1 = [10, 20, 30]
list2 = [40, 50, 60]
concatenated_list = list1 + list2
print("Concatenated List:", concatenated_list)

# 4. Membership Operator (Checking if an element exists in a list)
print("Is 20 in list1?", 20 in list1)
print("Is 100 in list1?", 100 in list1)

# 5. Iteration Over a List
print("Iterating over list1:")
for item in list1:
    print(item, end=" ")
print("\n")

# 6. Indexing and Slicing
sample_list = ['apple', 'banana', 'cherry', 'date', 'fig']
print("Element at index 2:", sample_list[2])  # Indexing
print("Slice from index 1 to 3:", sample_list[1:4])  # Slicing

# 7. List Methods (Add, Extend & Delete)
numbers = [1, 2, 3]
print("Original List:", numbers)

# Adding an element (append)
numbers.append(4)
print("After Append:", numbers)

# Extending a list
numbers.extend([5, 6, 7])
print("After Extend:", numbers)

# Deleting an element (remove & pop)
numbers.remove(2)  # Removes first occurrence of 2
print("After Removing 2:", numbers)

popped_item = numbers.pop(2)  # Removes element at index 2
print(f"After Pop at index 2 (Removed {popped_item}):", numbers)

# Deleting using 'del'
del numbers[0]  # Deletes element at index 0
print("After Deleting first element:", numbers)

# Clearing the list
numbers.clear()
print("After Clearing the list:", numbers)
