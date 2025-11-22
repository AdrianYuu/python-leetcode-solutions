class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        minimum = 0

        for num in nums:
            prev_step = num % 3
            next_step = 3 - num % 3
            minimum += min(prev_step, next_step)

        return minimum
       
"""
n = 8

8 % 3 = 2

Increase: 3 - 2 = 1
Decrease: 2
"""