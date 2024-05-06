Problem Statement: Matrix Subarray Sum

Given a matrix represented by a 2D list matrix, find the sum of all subarrays of the matrix. A subarray of a matrix is defined as a contiguous block of elements within the matrix.

Write a Python function called subarray_sum to solve this problem.

Function Signature:

python
Copy code
from typing import List

def subarray_sum(matrix: List[List[int]]) -> int:
pass
Input:

A 2D list matrix representing the input matrix. Each row of the matrix is represented by a list of integers.
Output:

An integer representing the sum of all subarrays of the input matrix.
Example:

python
Copy code

> > > subarray_sum([[1, 2], [3, 4]])
> > > 45
> > > Note:

You may assume that the input matrix is a non-empty 2D list.
The subarrays can have different dimensions, ranging from a single element to the entire matrix.
