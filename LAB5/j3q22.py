def input_array_elements(size):
    array = []
    print(f"Enter {size} elements for the array:")
    for i in range(size):
        element = int(input(f"Element at position {i}: "))
        array.append(element)
    return array

def print_alternate_elements(array):
    print("Every alternate element in the array is:")
    for i in range(0, len(array), 2):
        print(array[i])

def main():
    size = int(input("Enter the size of the array: "))
    
    array = input_array_elements(size)
    
    print_alternate_elements(array)

if __name__ == "__main__":
    main()
