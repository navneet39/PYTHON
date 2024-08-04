def input_float_array(size, array_number):
    array = []
    print(f"Enter the elements for array {array_number}:")
    for i in range(size):
        element = float(input(f"Element at position {i}: "))
        array.append(element)
    return array

def merge_arrays(array1, array2):
    return array1 + array2

def main():
    size1 = int(input("Enter the size of the first array: "))
    size2 = int(input("Enter the size of the second array: "))
    
    array1 = input_float_array(size1, 1)
    array2 = input_float_array(size2, 2)
    
    merged_array = merge_arrays(array1, array2)
    
    print("The merged array is:")
    print(merged_array)

if __name__ == "__main__":
    main()

