class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        used = set()

        def backtrack(curr_comb):
            if len(nums) == len(curr_comb):
                result.append(curr_comb.copy())
                return
            
            for i in range(len(nums)):
                if i in used:
                    continue
                used.add(i)
                curr_comb.append(nums[i])
                backtrack(curr_comb)
                curr_comb.pop()
                used.remove(i)
        
        backtrack([])
        return result