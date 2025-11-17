class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last_index = None

        for index, num in enumerate(nums):
            if num == 1:
                if last_index is not None:
                    if index - last_index - 1 < k:
                        return False

                last_index = index

        return True