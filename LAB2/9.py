#Write a python program to convert a Binary Number to Decimal and Decimal to Binary. 
def b_to_d(binary):
    decimal = int(binary, 2)
    return decimal

def d_to_b(decimal):
    binary = bin(decimal).replace("0b", "")
    return binary

print("1. Binary to Decimal")
print("2. Decimal to Binary")

choice = int(input("Enter your choice: "))

if choice == 1:
    binary = input("Enter a binary number: ")
    decimal = b_to_d(binary)
    print("The decimal equivalent of", binary, "is", decimal)
elif choice == 2:
    decimal = int(input("Enter a decimal number: "))
    binary = d_to_b(decimal)
    print("The binary equivalent of", decimal, "is", binary)
else:
    print("Invalid choice")