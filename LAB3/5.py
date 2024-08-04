def reverse_list(lst):
    reversed_lst = []
    for i in range(len(lst) - 1, -1, -1):
        reversed_lst.append(lst[i])
    return reversed_lst

try:

    num_elements = int(input("Enter the number of elements in the list: "))

    user_list = []
    
    for i in range(num_elements):
        element = input(f"Enter element {i + 1}: ")
        user_list.append(element)

    reversed_list = reverse_list(user_list)
    
    print("The reversed list is:")
    for element in reversed_list:
        print(element)
except ValueError:
    print("Invalid input. Please enter an integer for the number of elements.")
