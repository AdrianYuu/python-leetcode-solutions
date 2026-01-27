class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        target = {}
        letters = {}

        for c in ransomNote:
            if c not in target:
                target[c] = 1
            else:
                target[c] += 1
        
        for c in magazine:
            if c not in letters:
                letters[c] = 1
            else:
                letters[c] += 1
        
        for c in target:
            if c not in letters or letters[c] < target[c]:
                return False
        
        return True