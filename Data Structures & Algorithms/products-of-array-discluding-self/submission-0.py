class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zeroCount = 0
        for num in nums:
            if num == 0:
                zeroCount += 1
                continue
            product *= num
        if zeroCount > 1:
            return [0] * len(nums)
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = product
                continue
            if zeroCount == 1:
                nums[i] = 0
                continue
            print(nums[i], product)
            nums[i] = product//nums[i]
        return nums