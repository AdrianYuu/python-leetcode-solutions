class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        curr = 0
        length = len(bits)

        while curr < length - 1:
            curr += bits[curr] + 1

        return curr == length - 1