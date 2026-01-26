class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        diff = float("inf")
        
        for i in range(len(arr) - 1):
            diff = min(diff, abs(arr[i + 1] - arr[i]))

        result = []
        for i in range(len(arr) - 1):
            if abs(arr[i + 1] - arr[i]) == diff:
                result.append([arr[i], arr[i + 1]])

        return result