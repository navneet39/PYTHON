import math

def factorial_series(n):
    series = [math.factorial(i) for i in range(1, n + 1)]
    return series

n = int(input("Enter the number of terms: "))

series = factorial_series(n)

print("The series up to", n, "terms is:", series)