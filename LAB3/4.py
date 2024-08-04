def print_list(lst):
    for element in lst:
        print(element)

try:
    
    num_elements = int(input("Enter the number of elements in the list: "))
     
    user_list = []
    
    for i in range(num_elements):
        element = input(f"Enter element {i + 1}: ")
        user_list.append(element)
      
    print("The elements of the list are:")
    print_list(user_list)
except ValueError:
    print("Invalid input. Please enter an integer for the number of elements.")
