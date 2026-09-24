class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False

        count = [0] * 26
        l = 0
        for s in s1:
            count[ord(s) - ord('a')] += 1
        
        
        for r in range(len(s1) - 1, len(s2)):
            count2 = [0] * 26
            for i in range(l, r + 1):
                count2[ord(s2[i]) - ord('a')] += 1
            if count2 == count:
                return True
            l += 1
        
        return False
        
        