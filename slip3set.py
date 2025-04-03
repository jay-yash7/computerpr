# Set Operations in Python

# Creating sets
setA = {1, 2, 3, 4, 5}
setB = {4, 5, 6, 7, 8}

print("Set A:", setA)
print("Set B:", setB)

# 1. Union of sets
union_set = setA | setB  # OR use setA.union(setB)
print("Union of A and B:", union_set)

# 2. Intersection of sets
intersection_set = setA & setB  # OR use setA.intersection(setB)
print("Intersection of A and B:", intersection_set)

# 3. Difference of sets (Elements in A but not in B)
difference_set = setA - setB  # OR use setA.difference(setB)
print("Difference (A - B):", difference_set)

# 4. Difference of sets (Elements in B but not in A)
difference_set_BA = setB - setA
print("Difference (B - A):", difference_set_BA)

# 5. Symmetric Difference (Elements in either A or B but not both)
symmetric_diff_set = setA ^ setB  # OR use setA.symmetric_difference(setB)
print("Symmetric Difference:", symmetric_diff_set)

# 6. Subset check
subset_check = {1, 2}.issubset(setA)  
print("{1, 2} is subset of A:", subset_check)

# 7. Superset check
superset_check = setA.issuperset({1, 2})  
print("A is superset of {1, 2}:", superset_check)

# 8. Membership testing
print("Is 3 in Set A?", 3 in setA)
print("Is 10 in Set B?", 10 in setB)

# 9. Adding an element to a set
setA.add(10)
print("Set A after adding 10:", setA)

# 10. Removing an element from a set
setB.remove(8)  # Throws an error if element not found
print("Set B after removing 8:", setB)

# 11. Discarding an element (no error if not found)
setB.discard(15)  # No error even if 15 is not present
print("Set B after discarding 15:", setB)

# 12. Clearing a set
setA.clear()
print("Set A after clearing:", setA)
