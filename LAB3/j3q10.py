def input_array_elements(size):
    array = []
    for i in range(size):
        element = int(input(f"Enter element at position {i}: "))
        array.append(element)
    return array

def find_smallest_number(array):
    if len(array) == 0:
        return None  # Handle case when array is empty
    smallest = array[0]
    for num in array[1:]:
        if num < smallest:
            smallest = num
    return smallest

def main():
    size = int(input("Enter the number of elements in the array: "))
    if size <= 0:
        print("The array must have at least one element.")
        return
    
    array = input_array_elements(size)
    
    smallest_number = find_smallest_number(array)
    print("The smallest number in the array is:", smallest_number)

if __name__ == "__main__":
    main()
