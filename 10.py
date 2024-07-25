def fibonacci(n):
    fib_series = [0, 1]  # Initialize Fibonacci series with first two terms
    for _ in range(2, n):
        fib_series.append(fib_series[-1] + fib_series[-2])  # Add the last two terms
    return fib_series[:n]  # Return the first n terms of Fibonacci series

# Input from user
n = int(input("Enter the number of terms: "))

# Generate and print Fibonacci series
fib_series = fibonacci(n)
print(f"Fibonacci Series up to {n} terms:", fib_series)
