Problem Statement: Array Intersection

Given two integer arrays nums1 and nums2, return an array containing all the elements that appear in both arrays. The result should be in any order and should not contain duplicates.

Write a Python function called array_intersection to solve this problem.

Function Signature:

python
Copy code
from typing import List

def array_intersection(nums1: List[int], nums2: List[int]) -> List[int]:
pass
Input:

Two integer arrays nums1 and nums2, where 1 <= len(nums1), len(nums2) <= 1000.
Each array may contain duplicates.
Output:

A list of integers representing the intersection of nums1 and nums2.
Example:

python
Copy code

> > > array_intersection([1, 2, 2, 1], [2, 2])
> > > [2]
> > > array_intersection([4, 9, 5], [9, 4, 9, 8, 4])
> > > [9, 4]
> > > Note:

Each element in the result should appear as many times as it shows in both arrays.
You may return the result in any order.
The input arrays may contain duplicate elements, and the result should not contain duplicate elements.
