class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        length = len(heights)
        stack = [] # (height, left most index)
        max_a = 0

        for i, h in enumerate(heights):
            start = i # will be replaced with the last pop index (left most index)

            while stack and stack[-1][0] > h:
                height, index = stack.pop()
                max_a = max(max_a, height * (i - index))
                start = index

            stack.append((h, start))

        # remaining in the stack
        while stack:
            height, index = stack.pop()
            max_a = max(max_a, height * (length - index))

        return max_a