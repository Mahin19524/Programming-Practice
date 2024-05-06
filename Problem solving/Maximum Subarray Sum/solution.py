from typing import List

def subarray_sum(matrix: List[List[int]]) -> int:
    rows = len(matrix)
    cols = len(matrix[0])
    total_sum = 0
    
    # Iterate through all possible submatrices
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    # Calculate the sum of the submatrix
                    submatrix_sum = 0
                    for m in range(i, k + 1):
                        for n in range(j, l + 1):
                            submatrix_sum += matrix[m][n]
                    # Add the sum to the total_sum
                    total_sum += submatrix_sum
                    
    return total_sum

# Example usage:
matrix = [[1, 2], [3, 4]]
print(subarray_sum(matrix))  # Output: 45
