def input_array_elements(size):
    array = []
    for i in range(size):
        element = int(input(f"Enter element at position {i}: "))
        array.append(element)
    return array

def search_element(array, target):
    for index, element in enumerate(array):
        if element == target:
            return index
    return -1

def main():
    size = int(input("Enter the size of the array: "))
    print("Enter elements for the array:")
    array = input_array_elements(size)
    
    target = int(input("Enter the element to search for: "))
    index = search_element(array, target)
    
    if index != -1:
        print(f"Element {target} found at position {index}.")
    else:
        print(f"Element {target} not found in the array.")

if __name__ == "__main__":
    main()
