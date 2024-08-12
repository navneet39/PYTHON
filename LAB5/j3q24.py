def input_array_elements(size, array_number):
    array = []
    print(f"Enter {size} elements for array {array_number} (sorted in ascending order):")
    for i in range(size):
        element = int(input(f"Element at position {i}: "))
        array.append(element)
    return array

def merge_sorted_arrays(array1, array2):
    sorted_array = []
    i, j = 0, 0
    
    # Merge the two arrays
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            sorted_array.append(array1[i])
            i += 1
        else:
            sorted_array.append(array2[j])
            j += 1
    
    # Append remaining elements
    while i < len(array1):
        sorted_array.append(array1[i])
        i += 1
    
    while j < len(array2):
        sorted_array.append(array2[j])
        j += 1
    
    return sorted_array

def print_array(array):
    print("The merged sorted array is:")
    print(' '.join(map(str, array)))

def main():
    size1 = int(input("Enter the size of the first sorted array: "))
    size2 = int(input("Enter the size of the second sorted array: "))
    
    print("Input for the first array:")
    array1 = input_array_elements(size1, 1)
    
    print("Input for the second array:")
    array2 = input_array_elements(size2, 2)
    
    # Ensure both arrays are sorted
    if array1 != sorted(array1) or array2 != sorted(array2):
        print("Error: Both arrays must be sorted in ascending order.")
        return
    
    merged_array = merge_sorted_arrays(array1, array2)
    
    print_array(merged_array)

if __name__ == "__main__":
    main()
