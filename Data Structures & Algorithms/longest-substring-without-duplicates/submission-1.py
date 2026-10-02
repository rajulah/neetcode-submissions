class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        stringCharSet = set()
        left = 0
        right = 0
        longest = 0
        for right in range(len(s)):
            while s[right] in stringCharSet:
                stringCharSet.remove(s[left])
                left += 1
            stringCharSet.add(s[right])
            longest = max(longest, len(stringCharSet))
        return longest