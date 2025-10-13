class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        length = len(nums)

        for i in range(length):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = length - 1

            while left < right:
                sum = nums[i] + nums[left] + nums[right]

                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1

                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return result 