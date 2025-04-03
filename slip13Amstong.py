'''def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

num = int(input("Enter a number: "))
print("Factorial of", num, "is", factorial(num))
'''

def is_armstrong(n):
    digits = [int(d) for d in str(n)]
    return sum(d**len(digits) for d in digits) == n

num = int(input("Enter a number: "))
print(num, "is an Armstrong number" if is_armstrong(num) else "is not an Armstrong number")
