def display_table(N):
    for i in range(1, N + 1):
        print(f"{i} 1 {i} {i**2} {i**3}")

try:
    N = int(input("Enter a positive integer N: "))
    
    if N <= 0:
        print("Please enter a positive integer for N.")
    else:
        display_table(N)
except ValueError:
    print("Invalid input. Please enter a positive integer.")
