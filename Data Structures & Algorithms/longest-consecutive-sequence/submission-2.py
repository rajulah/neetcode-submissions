class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        hashMap = {}
        nums.sort()
        for i in range(len(nums)):
            hashMap[nums[i]] = i
        result = [1]*len(nums)

        for i in range(1,len(nums)):
            precedent = nums[i] - 1
            if precedent in hashMap and hashMap[precedent] < i:
                result[i] += result[hashMap[precedent]]
        return max(result)