class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        numeric = '0123456789'
        clean_str = ''

        for c in s:
            if c.lower() in alpha:
                clean_str += c.lower()
            elif c in numeric:
                clean_str += c

        length = len(clean_str)
        for i in range(length):
            if clean_str[i] != clean_str[length - 1 - i]:
                return False

        return True