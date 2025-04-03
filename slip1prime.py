### Program to print the multiplication table of a given number

# num = int(input("Enter a number: "))

# print(f"Multiplication Table of {num}:")
# for i in range(1, 11):
#     print(f"{num} x {i} = {num * i}")
# 

# Program to check if a number is prime

num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print(f"{num} is not a prime number")
            break
    else:
        print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
