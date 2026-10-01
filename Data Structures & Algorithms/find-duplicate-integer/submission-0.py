class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # nums -> n + 1 integers
        # each integer -> 1 <= num <= n
        # exacctly one int that repeats and others at most once
        # return that integer
        array = [0] * (len(nums)+1)
        for num in nums:
            array[num] += 1
            if array[num] > 1:
                return num
        return -1
