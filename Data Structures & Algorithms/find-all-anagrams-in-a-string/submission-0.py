class Solution:
    def getCharCounts(self, s: str):
        c = [0] * 26
        for char in s:
            c[ord(char) - ord('a')] += 1
        return c

    def findAnagrams(self, s: str, p: str) -> List[int]:
        # s -> string to check
        # p -> reference string
        # output -> start indices of all anagrams of p in s.
        # s = "baca", p = "ac"
        result = []
        p_counts = self.getCharCounts(p)
        right = len(p)
        s_char_counts = self.getCharCounts(s[:right])
        if p_counts == s_char_counts:
            result.append(0)
        left = 0
        for i in range(right, len(s)):
            s_char_counts[ord(s[i]) - ord('a')] += 1
            s_char_counts[ord(s[left]) - ord('a')] -= 1
            left += 1
            if s_char_counts == p_counts:
                result.append(left)
        
        return result

