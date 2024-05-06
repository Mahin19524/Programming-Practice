from typing import List

def transpose_matrix(matrix: List[List[int]]) -> List[List[int]]:
    # Get dimensions of the input matrix
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Initialize an empty matrix for the transpose
    transpose = [[0] * rows for _ in range(cols)]
    
    # Fill the transpose matrix by swapping rows and columns
    for i in range(rows):
        for j in range(cols):
            transpose[j][i] = matrix[i][j]
    
    return transpose

# Example usage:
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(transpose_matrix(matrix1))  # Output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

matrix2 = [[1, 2], [3, 4], [5, 6]]
print(transpose_matrix(matrix2))  # Output: [[1, 3, 5], [2, 4, 6]]
