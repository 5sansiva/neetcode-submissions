class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if not(len(s) == len(t)):
            return False

        letters = [0] * 26

        for c in range(len(s)):
            letters[ord(s[c]) - ord('a')] += 1
            letters[ord(t[c]) - ord('a')] -= 1

        for num in letters:
            if num > 0:
                return False
        return True
        