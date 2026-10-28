class Solution:
    def getCounts(self, s):
        c = [0]*26
        for char in s:
            c[ord(char)-ord('a')] += 1
        return c

    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        p_counts = self.getCounts(p)
        result = []
        s_counts = self.getCounts(s[:len(p)])
        if p_counts == s_counts:
            result.append(0)
        left = 0
        for right in range(len(p), len(s)):
            s_counts[ord(s[right]) - ord('a')] += 1
            s_counts[ord(s[left]) - ord('a')] -= 1
            left += 1
            if s_counts == p_counts:
                result.append(left)
        return result