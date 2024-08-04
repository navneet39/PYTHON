def series(n):
    series_sum = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            series_sum -= 1 / i
        else:
            series_sum += 1 / i
    return series_sum


try:
    n = int(input("Enter a positive integer n: "))
    
    if n <= 0:
        print("Please enter a positive integer.")
    else:
        result = series(n)
        print(f"The sum of the series up to {n} terms is: {result}")
except ValueError:
    print("Invalid input. Please enter a positive integer.")
