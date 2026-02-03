class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        subset = []

        def backtrack(i, sum):
            # found
            if sum == target:
                result.append(subset.copy())
                return

            # out of target or already 
            # reach the end of candidates
            if sum > target or i == len(candidates):
                return
            
            # use the current value
            subset.append(candidates[i])
            backtrack(i, sum + candidates[i])
            subset.pop()

            # don't use the current value
            backtrack(i + 1, sum)

        backtrack(0, 0)

        return result
