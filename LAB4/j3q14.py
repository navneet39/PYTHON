def input_array_elements(size):
    array = []
    for i in range(size):
        element = int(input(f"Enter element at position {i}: "))
        array.append(element)
    return array

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def count_primes(array):
    prime_count = 0
    for num in array:
        if is_prime(num):
            prime_count += 1
    return prime_count

def main():
    size = int(input("Enter the size of the array: "))
    array = input_array_elements(size)
    
    prime_count = count_primes(array)
    print("Number of prime numbers in the array:", prime_count)

if __name__ == "__main__":
    main()
