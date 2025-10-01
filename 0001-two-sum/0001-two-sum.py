class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remainder = {}

        for idx, num in enumerate(nums):
            if num in remainder:
                return [remainder[num], idx]
            
            diff = target - num
            remainder[diff] = idx