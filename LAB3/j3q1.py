def calculate_sum_average():
    
    n = int(input("Enter the number of elements in the array: "))

    array = []

    for i in range(n):
        element = int(input(f"Enter element {i+1}: "))
        array.append(element)

    total_sum = sum(array)

    average = total_sum / n

    print(f"Sum of the array elements: {total_sum}")
    print(f"Average of the array elements: {average:.2f}")

calculate_sum_average()
