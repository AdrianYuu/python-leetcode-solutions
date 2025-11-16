class Solution:
    def numSub(self, s: str) -> int:
        count = 0
        result = 0

        for c in s:
            if c == '0':
                result += (count * (count + 1) // 2)
                count = 0
            else:
                count += 1

        result += (count * (count + 1) // 2)

        return result % (10**9 + 7)