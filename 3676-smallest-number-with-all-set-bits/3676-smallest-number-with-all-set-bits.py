class Solution:
    def smallestNumber(self, n: int) -> int:
        num = 1

        while num < n:
            num = num * 2 + 1

        return num