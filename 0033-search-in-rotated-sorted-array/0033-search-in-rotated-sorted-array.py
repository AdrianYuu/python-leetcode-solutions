class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def get_min_idx(left, right):
            while left <= right:
                mid = left + (right - left) // 2

                if nums[mid] < nums[mid - 1]:
                    return mid

                if nums[mid] > nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

            return left

        left = 0
        right = len(nums) - 1
        min_idx = get_min_idx(left, right)

        print(f'Min Idx: {min_idx}')

        # must be on the second array
        if target < nums[0]:
            left = min_idx
        # must be on the first array but only update if its have 2 part of array
        elif min_idx != left:
            right = min_idx - 1

        # do another binary search based on the condition
        while left <= right:
            mid = left + (right - left) // 2

            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                return mid
        
        return -1