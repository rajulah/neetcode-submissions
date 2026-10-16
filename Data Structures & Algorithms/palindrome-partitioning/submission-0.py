class Solution:
    def isPalindrome(self, s: str)-> bool:
        return s==s[::-1]
    def partition(self, s: str) -> List[List[str]]:
        result = []
        curr_partition = []

        def backtrack(start):
            if start == len(s):
                result.append(curr_partition.copy())
                return
            
            for end in range(start, len(s)):
                substring = s[start:end+1]
                if not self.isPalindrome(substring):
                    continue
                curr_partition.append(substring)
                backtrack(end+1)
                curr_partition.pop()
        backtrack(0)
        return result