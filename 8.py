# Function to check if a number is a palindrome
def is_palindrome(number):
    # Convert number to string and check if it reads the same forwards and backwards
    return str(number) == str(number)[::-1]

# Take user input for the number
number = input("Enter a number: ")

# Check if the number is a palindrome
if is_palindrome(number):
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")
