class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        total = sum(nums)
        partition = 0
        current = 0

        for i in range(len(nums) - 1):
            current += nums[i]
            total -= nums[i]

            is_even = (total - current) % 2 == 0

            if is_even:
                partition += 1

        return partition