class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        for i in range(len(nums)):
            curr = -1 * nums[i]
            seen = {}
            for j in range(len(nums)):
                if j == i:
                    continue
                complement = curr - nums[j]
                if complement in seen:
                    foundSet = sorted([nums[i],nums[j],complement])
                    if foundSet not in result:
                        result.append(foundSet)
                seen[nums[j]] = j
        return result
