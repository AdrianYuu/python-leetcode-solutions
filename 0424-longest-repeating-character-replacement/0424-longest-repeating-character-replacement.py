class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        result = 0
        occ = [0] * 26

        for right in range(len(s)):
            occ[ord(s[right]) - 65] += 1

            max_occ = max(occ)

            while (right - left + 1) - max_occ > k:
                occ[ord(s[left]) - 65] -= 1
                left += 1

            result = max(result, right - left + 1)

        return result