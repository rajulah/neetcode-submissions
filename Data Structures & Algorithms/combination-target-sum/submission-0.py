class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # arr of distinct integers nums
        # unique combinations of sum = target
        result = []
        def backtrack(start, curr_path, target):
            if target == 0:
                result.append(curr_path.copy())
                return
            if target < 0:
                return
            for i in range(start, len(nums)):
                curr_path.append(nums[i])
                backtrack(i, curr_path, target - nums[i])
                curr_path.pop()
        backtrack(0, [], target)

        return result