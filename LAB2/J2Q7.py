def count_digits(n):
    count = 0
    while n != 0:
        n = n // 10
        count += 1
    return count

num = int(input("Enter an integer: "))

digit_count = count_digits(num)

print("The number of digits in", num, "is", digit_count)