def input_2d_array(rows, cols):
    matrix = []
    print(f"Enter the elements for a {rows}x{cols} matrix:")
    for i in range(rows):
        row = []
        for j in range(cols):
            element = int(input(f"Element [{i+1},{j+1}]: "))
            row.append(element)
        matrix.append(row)
    return matrix

def sum_of_odd_numbers(matrix):
    total_sum = 0
    for row in matrix:
        for element in row:
            if element % 2 != 0:
                total_sum += element
    return total_sum

def main():
    rows = int(input("Enter the number of rows for the matrix: "))
    cols = int(input("Enter the number of columns for the matrix: "))
    
    matrix = input_2d_array(rows, cols)
    
    print("The matrix is:")
    for row in matrix:
        print(row)
    
    odd_sum = sum_of_odd_numbers(matrix)
    print("The sum of all odd numbers in the matrix is:", odd_sum)

if __name__ == "__main__":
    main()
