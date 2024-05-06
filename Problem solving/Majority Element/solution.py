from typing import List

def majority_element(nums: List[int]) -> int:
    candidate = None
    count = 0
    
    # Find potential candidate for majority element
    for num in nums:
        if count == 0:
            candidate = num
        if num == candidate:
            count += 1
        else:
            count -= 1
    
    # Verify if candidate is the majority element
    count = 0
    for num in nums:
        if num == candidate:
            count += 1
    if count > len(nums) // 2:
        return candidate
    else:
        raise ValueError("No majority element found in the array.")

# Example usage:
print(majority_element([3, 2, 3]))  # Output: 3
print(majority_element([2, 2, 1, 1, 1, 2, 2]))  # Output: 2
