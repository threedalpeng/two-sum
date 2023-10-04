from typing import List

def twoSum(self, nums: List[int], target: int) -> List[int]:

    for i, f in enumerate(nums):
        for j, s in enumerate(nums[i + 1:]):
            if f + s == target:
                return [i, i + 1 + j]
    
    return []
