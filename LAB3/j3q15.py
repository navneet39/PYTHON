def input_array_elements(size):
    array = []
    for i in range(size):
        element = int(input(f"Enter element at position {i}: "))
        array.append(element)
    return array

def find_second_highest(array):
    if len(array) < 2:
        return None  # Not enough elements to find the second highest
    
    first = second = float('-inf')
    
    for num in array:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    
    return second if second != float('-inf') else None

def main():
    size = int(input("Enter the size of the array: "))
    if size < 2:
        print("Array must contain at least two elements.")
        return
    
    array = input_array_elements(size)
    
    second_highest = find_second_highest(array)
    
    if second_highest is not None:
        print("The second highest element in the array is:", second_highest)
    else:
        print("There is no second highest element (all elements might be the same).")

if __name__ == "__main__":
    main()
