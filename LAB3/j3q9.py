def input_array_elements(size):
    array = []
    for i in range(size):
        element = int(input(f"Enter element at position {i}: "))
        array.append(element)
    return array

def reverse_array(array):
    left = 0
    right = len(array) - 1
    while left < right:
        # Swap the elements at the left and right indices
        array[left], array[right] = array[right], array[left]
        left += 1
        right -= 1

def main():
    size = int(input("Enter the size of the array: "))
    array = input_array_elements(size)
    
    print("Original array:", array)
    reverse_array(array)
    print("Reversed array:", array)

if __name__ == "__main__":
    main()
