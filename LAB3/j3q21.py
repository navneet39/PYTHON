def input_array_elements(size):
    array = []
    print(f"Enter {size} elements for the array:")
    for i in range(size):
        element = int(input(f"Element at position {i}: "))
        array.append(element)
    return array

def find_duplicates_with_frequency(array):
    frequency = {}
    duplicates = {}
    
    # Count the frequency of each element
    for num in array:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    
    # Identify duplicates and their frequencies
    for num, count in frequency.items():
        if count > 1:
            duplicates[num] = count
    
    return duplicates

def main():
    size = int(input("Enter the size of the array: "))
    
    array = input_array_elements(size)
    
    duplicates = find_duplicates_with_frequency(array)
    
    if duplicates:
        print("Duplicate elements and their frequencies:")
        for element, freq in duplicates.items():
            print(f"Element {element} occurs {freq} times")
    else:
        print("No duplicate elements found.")

if __name__ == "__main__":
    main()
