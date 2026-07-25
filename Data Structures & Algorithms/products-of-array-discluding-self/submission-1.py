class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [0]*n
        suff = [0]*n
        result = [0]*n
        pref[0] = 1
        suff[n-1] = 1
        for i in range(1, n):
            pref[i] = pref[i-1] * nums[i-1]
        for i in range(n-2, -1, -1):
            suff[i] = nums[i+1] * suff[i+1]
        for i in range(n):
            result[i] = pref[i] * suff[i]
        return result
        # product = 1
        # zeroCount = 0
        # for num in nums:
        #     if num == 0:
        #         zeroCount += 1
        #         continue
        #     product *= num
        # if zeroCount > 1:
        #     return [0] * len(nums)
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         nums[i] = product
        #         continue
        #     if zeroCount == 1:
        #         nums[i] = 0
        #         continue
        #     print(nums[i], product)
        #     nums[i] = product//nums[i]
        # return nums