def input_array_elements(size):
    array = []
    for i in range(size):
        element = int(input(f"Enter element at position {i}: "))
        array.append(element)
    return array

def find_array_range(array):
    if len(array) == 0:
        return 0
    min_val = array[0]
    max_val = array[0]
    for num in array[1:]:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
    return max_val - min_val

def main():
    size = int(input("Enter the size of the array: "))
    print("Enter elements for the array:")
    array = input_array_elements(size)
    array_range = find_array_range(array)
    print("The range of the array is:", array_range)

if __name__ == "__main__":
    main()
