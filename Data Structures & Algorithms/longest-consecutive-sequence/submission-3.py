class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        nums = set(nums)
        seen = set()
        for num in nums:
            if num in seen:
                continue
            length = 1
            while num + 1 in nums:
                length += 1
                num += 1
            seen.add(num)
            longest = max(longest,length)
        return longest






        # if len(nums) < 1:
        #     return 0
        # hashMap = {}
        # nums.sort()
        # for i in range(len(nums)):
        #     hashMap[nums[i]] = i
        # result = [1]*len(nums)

        # for i in range(1,len(nums)):
        #     precedent = nums[i] - 1
        #     if precedent in hashMap and hashMap[precedent] < i:
        #         result[i] += result[hashMap[precedent]]
        # return max(result)