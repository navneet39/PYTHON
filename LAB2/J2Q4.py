def sum_of_natural_numbers(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum

n = int(input("Enter a positive integer: "))

if n <= 0:
    print("Please enter a positive integer.")
else:
    result = sum_of_natural_numbers(n)
    print("The sum of natural numbers up to", n, "is", result)
    