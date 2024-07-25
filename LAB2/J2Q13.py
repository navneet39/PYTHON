m = int(input("Enter the first integer: "))
n = int(input("Enter the second integer: "))

if m % n == 0:
    print(f"{m} is a multiple of {n}.")
else:
    print(f"{m} is not a multiple of {n}.")