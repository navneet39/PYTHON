def input_array_elements(size, array_number):
    array = []
    print(f"Enter the elements for array {array_number}:")
    for i in range(size):
        element = int(input(f"Element at position {i}: "))
        array.append(element)
    return array

def add_arrays_index_wise(array1, array2):
    size = len(array1)
    result_array = []
    for i in range(size):
        result_array.append(array1[i] + array2[i])
    return result_array

def main():
    size = int(input("Enter the size of the arrays: "))
    
    print("Input for the first array:")
    array1 = input_array_elements(size, 1)
    
    print("Input for the second array:")
    array2 = input_array_elements(size, 2)
    
    if len(array1) != len(array2):
        print("Error: Arrays must be of the same size.")
        return
    
    result_array = add_arrays_index_wise(array1, array2)
    
    print("The resulting array after adding elements index-wise is:")
    print(result_array)

if __name__ == "__main__":
    main()
