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

def is_sparse(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    total_elements = rows * cols
    zero_count = 0
    
    for row in matrix:
        zero_count += row.count(0)
    
    return zero_count > total_elements / 2

def main():
    rows = int(input("Enter the number of rows for the matrix: "))
    cols = int(input("Enter the number of columns for the matrix: "))
    
    matrix = input_matrix(rows, cols)
    
    print("The matrix is:")
    for row in matrix:
        print(' '.join(map(str, row)))
    
    if is_sparse(matrix):
        print("The matrix is sparse.")
    else:
        print("The matrix is not sparse.")

if __name__ == "__main__":
    main()
