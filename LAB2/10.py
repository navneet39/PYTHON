import math


def is_krishnamurthy(n):
    sum_of_factorials = 0
    for digit in str(n):
        sum_of_factorials += math.factorial(int(digit))
    return sum_of_factorials == n

input_num = int(input("Enter a number: "))
print(is_krishnamurthy(input_num))