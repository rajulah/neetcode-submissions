class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # input -> s : string
        # return -> len(longest substring without repeating chars)
        if s is None or s == "":
            return 0
        left = 0
        right = 1
        longest = 1
        curr_long_set = {s[0]: left}
        while right < len(s):
            # print("before- ", s[right],  left, right, s[left:right+1], curr_long_set)
            if s[right] in curr_long_set:
                left = max(left, curr_long_set[s[right]] + 1)
            curr_long_set[s[right]] = right
            if right - left + 1 > longest:
                # print(" if ")
                longest = right - left + 1
            # print("after- ", s[right], left, right, s[left:right+1], curr_long_set)

            right += 1
        return longest

