class Solution:
    def getCounts(self, s: str):
        c = [0] * 26
        for char in s:
            c[ord(char) - ord('a')] += 1
        return tuple(c)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            counts = self.getCounts(s)
            if counts in anagrams:
                anagrams[counts].append(s)
            else:
                anagrams[counts] = [s]
        return list(anagrams.values())
        
        

