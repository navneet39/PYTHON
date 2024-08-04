def input_matrix(rows, cols, matrix_number):
    matrix = []
    print(f"Enter the elements for matrix {matrix_number}:")
    for i in range(rows):
        row = []
        for j in range(cols):
            element = int(input(f"Element [{i+1},{j+1}]: "))
            row.append(element)
        matrix.append(row)
    return matrix

def subtract_matrices(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0])
    
    # Initialize result matrix with zeros
    result = [[0] * cols for _ in range(rows)]
    
    # Perform matrix subtraction
    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix1[i][j] - matrix2[i][j]
    
    return result

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))

def main():
    rows = int(input("Enter the number of rows for the matrices: "))
    cols = int(input("Enter the number of columns for the matrices: "))
    
    print("Input for the first matrix:")
    matrix1 = input_matrix(rows, cols, 1)
    
    print("Input for the second matrix:")
    matrix2 = input_matrix(rows, cols, 2)
    
    # Ensure both matrices have the same dimensions
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print("Error: Matrices must have the same dimensions for subtraction.")
        return
    
    result = subtract_matrices(matrix1, matrix2)
    
    print("The resulting matrix after subtraction is:")
    print_matrix(result)

if __name__ == "__main__":
    main()
