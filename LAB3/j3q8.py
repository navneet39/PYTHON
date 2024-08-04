def input_matrix(size):
    matrix = []
    print(f"Enter the elements for a {size}x{size} matrix:")
    for i in range(size):
        row = []
        for j in range(size):
            element = int(input(f"Element [{i+1},{j+1}]: "))
            row.append(element)
        matrix.append(row)
    return matrix

def sum_of_diagonal_elements(matrix):
    size = len(matrix)
    diagonal_sum = 0
    for i in range(size):
        diagonal_sum += matrix[i][i]  # Sum of primary diagonal elements
    return diagonal_sum

def main():
    size = int(input("Enter the size of the square matrix: "))
    matrix = input_matrix(size)
    
    print("The matrix is:")
    for row in matrix:
        print(row)
    
    diagonal_sum = sum_of_diagonal_elements(matrix)
    print("The sum of the diagonal elements is:", diagonal_sum)

if __name__ == "__main__":
    main()
