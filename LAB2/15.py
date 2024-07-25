def calculate_power(base, exponent):
    result = 1
    for _ in range(abs(exponent)):
        result *= base
    if exponent < 0:
        return 1 / result
    else:
        return result

base = float(input("Enter the base number: "))
exponent = int(input("Enter the exponent: "))

result = calculate_power(base, exponent)

print("The result of", base, "to the power of", exponent, "is:", result)