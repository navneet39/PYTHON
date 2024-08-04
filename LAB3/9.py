def print_pattern(N):
    for i in range(1, N + 1):
    
        print(" " * (N - i) + " . ")
         
        for j in range(i):
            spaces = " " * (N - i)
            if j == 0:
                print(spaces + "/ \\")
            else:
                print(spaces + "/" + " " * (2 * j) + "\\")
        
       
        if i > 1:
            print(spaces + "/" + "_" * (2 * j) + "\\")

        
        if i != N:
            print()


try:
    N = int(input("Enter a positive integer N: "))
    
    if N <= 0:
        print("Please enter a positive integer for N.")
    else:
        print_pattern(N)
except ValueError:
    print("Invalid input. Please enter a positive integer.")
