def input_array_elements(size):
    array = []
    for i in range(size):
        element = int(input(f"Enter element at position {i}: "))
        array.append(element)
    return array

def count_non_zero_elements(array):
    non_zero_count = 0
    for num in array:
        if num != 0:
            non_zero_count += 1
    return non_zero_count

def main():
    size = int(input("Enter the size of the array: "))
    array = input_array_elements(size)
    
    non_zero_count = count_non_zero_elements(array)
    print("Number of non-zero elements in the array:", non_zero_count)

if __name__ == "__main__":
    main()
