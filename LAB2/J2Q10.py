def find_median(numbers):
    numbers = sorted(numbers)
    n = len(numbers)
    if n % 2 == 1:
        median = numbers[n // 2]
    else:
        median = (numbers[n // 2 - 1] + numbers[n // 2]) / 2
    return median

numbers = input("Enter a set of numbers separated by space: ")
numbers = list(map(int, numbers.split()))

median = find_median(numbers)
print("The median of the set is:", median)