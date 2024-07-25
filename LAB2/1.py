import math

def sum_of_square_roots():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    num3 = float(input("Enter third number: "))
    sum_of_roots = math.sqrt(num1) + math.sqrt(num2) + math.sqrt(num3)
    print("Sum of square roots:", sum_of_roots)

sum_of_square_roots()