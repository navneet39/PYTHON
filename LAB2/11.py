def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

input_num = int(input("Enter a number: "))
print(sum_of_digits(input_num))