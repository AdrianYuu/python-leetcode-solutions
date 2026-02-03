class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []

        def backtrack(i):
            # out of bound (meaning on the leaf)
            if i == len(nums):
                result.append(subset.copy())
                return

            # use the current value
            subset.append(nums[i])
            # and do backtrack again
            backtrack(i + 1)
            # after that remove the value again
            subset.pop()

            # dont use the current value
            # just skip it
            backtrack(i + 1)

        backtrack(0)

        return result