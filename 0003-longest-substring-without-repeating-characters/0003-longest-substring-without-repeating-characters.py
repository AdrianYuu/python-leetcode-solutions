class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        result = 0

        for right in range(len(s)):
            # while the character on the right already exists in the set
            # we remove the most left and increment it
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            
            # if there is no duplicate anymore add the s[right]
            char_set.add(s[right])

            result = max(result, len(char_set))

        return result