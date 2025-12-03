class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # first binary search to find the row where the target might be exists
        left = 0
        right = len(matrix) - 1
        row = -1
        n = len(matrix[0]) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if target > matrix[mid][0]:
                row = mid

            # on the left
            if target < matrix[mid][0]:
                right = mid - 1
            # on the right
            elif target > matrix[mid][0]:
                left = mid + 1
            # maybe the target is on the first index
            else:
                return True

        # binary search in the row where the target might be exists
        left = 0
        right = len(matrix[row]) - 1

        while left <= right:
            mid = left + (right - left) // 2

            # on the left
            if target < matrix[row][mid]:
                right = mid - 1
            # on the right
            elif target > matrix[row][mid]:
                left = mid + 1
            else:
                return True
        
        return False