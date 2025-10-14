class Solution:
    def maxArea(self, height: List[int]) -> int:
        length = len(height)
        left = 0
        right = length - 1
        highest = max(height)
        max_area = 0

        while left < right:
            width = right - left
            area = width * min(height[left], height[right])
            max_area = max(max_area, area)

            if highest * width < max_area:
                break

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area