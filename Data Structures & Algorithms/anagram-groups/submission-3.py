class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = {}
        output = []

        for i in strs:
            key = i[:]
            key = ''.join(sorted(key))
            if key in anagrams:
                anagrams[key].append(i)
            else:
                anagrams[key] = [i]
        
        for v in anagrams.values():
            output.append(v)
        
        return output

        



        