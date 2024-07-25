n = int(input("Enter the upper limit: "))

print(f"Prime numbers up to {n} are:")

for number in range(2, n + 1):
    is_prime = True
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        print(number)
