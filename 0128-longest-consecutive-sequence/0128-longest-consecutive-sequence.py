class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0

        for num in nums:
            before = num - 1
            
            if before in nums:
                continue

            count = 0

            while True:
                after = num + count + 1
                if after in nums:
                    count += 1
                else:
                    break

            longest = max(longest, count + 1)

        return longest