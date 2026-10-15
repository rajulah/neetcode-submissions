class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        def backtrack(start, curr_comb):
            result.append(curr_comb.copy())
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                curr_comb.append(nums[i])
                backtrack(i+1, curr_comb)
                curr_comb.pop()
        backtrack(0,[])
        return result