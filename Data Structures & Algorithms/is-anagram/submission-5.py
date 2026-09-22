class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if not(len(s) == len(t)):
            return False

        letters = [0] * 26

        for c in s:
            letters[ord(c) - ord('a')] += 1
        
        for d in t:
            letters[ord(d) - ord('a')] -= 1

        for num in letters:
            if num > 0:
                return False
        return True
        