def find_lcm(a, b):
    hcf = find_hcf(a, b)
    lcm = (a * b) // hcf
    return lcm

def find_hcf(a, b):
    while b!= 0:
        a, b = b, a % b
    return a

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

lcm = find_lcm(num1, num2)

print("The LCM of", num1, "and", num2, "is", lcm)