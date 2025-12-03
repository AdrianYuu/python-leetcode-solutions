class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            print(nums[mid])

            # on the left
            if target < nums[mid]:
                right = mid - 1
            # on the right
            elif target > nums[mid]:
                left = mid + 1
            # found on mid
            else:
                return mid

        return -1