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

def multiply_matrices(matrix1, matrix2):
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    rows2 = len(matrix2)
    cols2 = len(matrix2[0])

    if cols1 != rows2:
        raise ValueError("Number of columns of the first matrix must be equal to the number of rows of the second matrix.")
    
    # Initialize result matrix with zeros
    result = [[0] * cols2 for _ in range(rows1)]
    
    # Perform matrix multiplication
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    
    return result

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))

def main():
    rows1 = int(input("Enter the number of rows for the first matrix: "))
    cols1 = int(input("Enter the number of columns for the first matrix: "))
    rows2 = int(input("Enter the number of rows for the second matrix: "))
    cols2 = int(input("Enter the number of columns for the second matrix: "))

    if cols1 != rows2:
        print("Error: Number of columns of the first matrix must be equal to the number of rows of the second matrix.")
        return
    
    matrix1 = input_matrix(rows1, cols1, 1)
    matrix2 = input_matrix(rows2, cols2, 2)
    
    result = multiply_matrices(matrix1, matrix2)
    
    print("The resulting matrix after multiplication is:")
    print_matrix(result)

if __name__ == "__main__":
    main()
