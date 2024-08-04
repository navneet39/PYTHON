def input_array_elements(size):
    array = []
    for i in range(size):
        element = int(input(f"Enter element at position {i}: "))
        array.append(element)
    return array

def sum_of_even_numbers(array):
    sum_even = 0
    for num in array:
        if num % 2 == 0:
            sum_even += num
    return sum_even

def main():
    size = int(input("Enter the size of the array: "))
    print("Enter elements for the array:")
    array = input_array_elements(size)
    
    sum_even = sum_of_even_numbers(array)
    print("The sum of even numbers in the array is:", sum_even)

if __name__ == "__main__":
    main()
