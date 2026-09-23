class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        count = [0] * 26
        maxFreq = 0
        maxLength = 0
        for r in range(len(s)):
            count[ord(s[r]) - ord('A')] += 1
            maxFreq = max(maxFreq, count[ord(s[r]) - ord('A')])
            replacements = (r - l + 1) - maxFreq
            if replacements > k:
                count[ord(s[l]) - ord('A')] -= 1
                l += 1
                continue
            maxLength = max(maxLength, r - l + 1)
        return maxLength
        


