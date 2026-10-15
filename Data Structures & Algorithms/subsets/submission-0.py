class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(start, curr_path):
            result.append(curr_path.copy()) #important. cz list is mutable
            for i in range(start, len(nums)):
                curr_path.append(nums[i])
                backtrack(i+1, curr_path)
                curr_path.pop()
        backtrack(0, [])
        return result       