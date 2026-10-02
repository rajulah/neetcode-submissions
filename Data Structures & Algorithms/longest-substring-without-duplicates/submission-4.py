class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charIndexMap = {}
        left = 0
        right = 0
        longest = 0
        for right in range(len(s)):
            if s[right] in charIndexMap:
                left = max(charIndexMap[s[right]] + 1, left)
            charIndexMap[s[right]] = right
            longest = max(longest, right - left + 1)
        return longest