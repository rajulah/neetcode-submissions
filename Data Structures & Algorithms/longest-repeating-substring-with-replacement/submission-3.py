class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqCount = defaultdict(int)
        left = 0
        maxFreq = 0
        longestStr = float("-inf")

        for right in range(len(s)):
            freqCount[s[right]] += 1
            maxFreq = max(maxFreq, freqCount[s[right]])

            if (right - left + 1) - maxFreq > k:
                freqCount[s[left]] -= 1
                left += 1
            longestStr = max(longestStr, right - left + 1)

        if longestStr == float("-inf"):
            return len(s)
        return longestStr