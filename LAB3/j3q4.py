def get_matrix(rows, cols):
    matrix = []
    print(f"Enter the elements for a {rows}x{cols} matrix:")
    for i in range(rows):
        row = []
        for j in range(cols):
            element = int(input(f"Element [{i+1},{j+1}]: "))
            row.append(element)
        matrix.append(row)
    return matrix

def display_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))

def add_matrices(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0])
    result = [[0 for _ in range(cols)] for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix1[i][j] + matrix2[i][j]
    
    return result

def main():
    rows = int(input("Enter the number of rows for the matrices: "))
    cols = int(input("Enter the number of columns for the matrices: "))

    print("Matrix 1:")
    matrix1 = get_matrix(rows, cols)
    print("Matrix 2:")
    matrix2 = get_matrix(rows, cols)

    print("Matrix 1:")
    display_matrix(matrix1)
    print("Matrix 2:")
    display_matrix(matrix2)

    sum_matrix = add_matrices(matrix1, matrix2)

    print("Sum of Matrix 1 and Matrix 2:")
    display_matrix(sum_matrix)

if __name__ == "__main__":
    main()
