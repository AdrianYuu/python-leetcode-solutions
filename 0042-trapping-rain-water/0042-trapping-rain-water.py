class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        left = 0
        right = length - 1
        max_left = height[left]
        max_right = height[right]

        trapped = 0

        while left < right:
            if max_left <= max_right:
                left += 1
                trapped += max(max_left - height[left], 0)
                max_left = max(max_left, height[left])
            else:
                right -= 1
                trapped += max(max_right - height[right], 0)
                max_right = max(max_right, height[right])

        return trapped