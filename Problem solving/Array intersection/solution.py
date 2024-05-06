from typing import List

def array_intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    # Convert lists to sets to remove duplicates
    set1 = set(nums1)
    set2 = set(nums2)
    
    # Find intersection of the two sets
    intersection = set1.intersection(set2)
    
    # Convert set back to list
    return list(intersection)
