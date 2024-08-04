def input_matrix(rows, cols):
    matrix = []
    print(f"Enter the elements for a {rows}x{cols} matrix:")
    for i in range(rows):
        row = []
        for j in range(cols):
            element = int(input(f"Element [{i+1},{j+1}]: "))
            row.append(element)
        matrix.append(row)
    return matrix

def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    transposed = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        transposed.append(new_row)
    return transposed

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))

def main():
    rows = int(input("Enter the number of rows for the matrix: "))
    cols = int(input("Enter the number of columns for the matrix: "))
    
    matrix = input_matrix(rows, cols)
    
    print("Original matrix:")
    print_matrix(matrix)
    
    transposed = transpose_matrix(matrix)
    
    print("Transposed matrix:")
    print_matrix(transposed)

if __name__ == "__main__":
    main()
