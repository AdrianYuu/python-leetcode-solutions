class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)

        if length == 1:
            return nums[0]
        
        if length == 2:
            return max(nums[0], nums[1])

        dp = [0] * length
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, length):
            dp[i] = max(
                nums[i] + dp[i - 2], # take current house
                dp[i - 1] # skip current house
            )

        print(dp)

        return dp[length - 1]