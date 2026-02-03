class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        subset = []
        candidates.sort()

        def backtrack(i, sum):
            if sum == target:
                result.append(subset.copy())
                return

            if sum > target or i == len(candidates):
                return

            # we take the value
            subset.append(candidates[i])
            backtrack(i + 1, sum + candidates[i])
            subset.pop()

            while i < len(candidates) - 1 and candidates[i] == candidates[i + 1]:
                i += 1

            # we don't take the value
            backtrack(i + 1, sum)

        backtrack(0, 0)

        return result