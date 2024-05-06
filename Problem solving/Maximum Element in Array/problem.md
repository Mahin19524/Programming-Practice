Problem Statement: Matrix Transpose

Given a matrix represented by a 2D list matrix, return the transpose of the matrix. The transpose of a matrix is obtained by swapping the rows and columns of the matrix. In other words, the rows of the original matrix become the columns of the transposed matrix, and vice versa.

Write a Python function called transpose_matrix to solve this problem.

Function Signature:

python
Copy code
from typing import List

def transpose_matrix(matrix: List[List[int]]) -> List[List[int]]:
pass
Input:

A 2D list matrix representing the input matrix. Each row of the matrix is represented by a list of integers.
Output:

A 2D list representing the transpose of the input matrix.
Example:

python
Copy code

> > > transpose_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
> > > [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
> > > transpose_matrix([[1, 2], [3, 4], [5, 6]])
> > > [[1, 3, 5], [2, 4, 6]]
> > > Note:

You may assume that the input matrix is a non-empty 2D list.
The input matrix may have a different number of rows and columns.
The output matrix should have the same number of rows as the number of columns in the input matrix, and vice versa.
