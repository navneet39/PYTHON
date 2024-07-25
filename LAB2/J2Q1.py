def is_buzz(n):
    if n % 10 == 7 or '7' in str(n):
        return True
    else:
        return False

num = int(input("Enter a number: "))

if is_buzz(num):
    print(num, "is a Buzz number.")
else:
    print(num, "is not a Buzz number.")