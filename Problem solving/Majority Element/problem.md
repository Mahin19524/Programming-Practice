Problem Statement: Majority Element

Given an array of integers nums, find the majority element. The majority element is the element that appears more than n // 2 times, where n is the length of the array. You may assume that the majority element always exists in the array.

Write a Python function called majority_element to solve this problem.

Function Signature:

python
Copy code
from typing import List

def majority_element(nums: List[int]) -> int:
pass
Input:

An integer array nums where 1 <= len(nums) <= 10^5.
Each integer in the array is between -10^9 and 10^9.
Output:

An integer representing the majority element in the array.
Example:

python
Copy code

> > > majority_element([3, 2, 3])
> > > 3
> > > majority_element([2, 2, 1, 1, 1, 2, 2])
> > > 2
> > > Note:

You may assume that the array will always contain a majority element.
You may assume that the majority element will be unique in the array.
The majority element is guaranteed to appear more than n // 2 times, where n is the length of the array.
