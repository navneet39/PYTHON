import math

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        fact = 1
        for i in range(2, n + 1):
            fact *= i
        return fact

def compute_cosine(x, n):
    cosine_sum = 0
    for i in range(n):
        term = ((-1) ** i) * (x ** (2 * i)) / factorial(2 * i)
        cosine_sum += term
    return cosine_sum

try:
    x = float(input("Enter the value of x (in radians): "))
    n = int(input("Enter a positive integer n: "))

    if n <= 0:
        print("Please enter a positive integer for n.")
    else:
        result = compute_cosine(x, n)
        print(f"The cosine of {x} using {n} terms is: {result}")
except ValueError:
    print("Invalid input. Please enter numerical values for x and n.")