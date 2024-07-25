import math

def cal_exp(base, exponent):
    result = math.pow(base, exponent)
    return result

base = float(input("Enter the base: "))
exponent = float(input("Enter the exponent: "))

result = cal_exp(base, exponent)

print("The exponential of", base, "raised to the power of", exponent, "is", result)