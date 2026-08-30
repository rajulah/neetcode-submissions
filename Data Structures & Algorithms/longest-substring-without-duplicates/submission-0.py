class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 1:
            return 0
        longestString = s[0]
        currLongestString = longestString
        for i in range(1,len(s)):
            if s[i] in currLongestString:
                j = 0
                while currLongestString[j] != s[i]:
                    j += 1
                currLongestString = currLongestString[j+1:]
            currLongestString = currLongestString + s[i]
            if len(currLongestString) > len(longestString):
                longestString = currLongestString
        return len(longestString)
            



