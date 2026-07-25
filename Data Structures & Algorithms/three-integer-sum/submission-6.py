class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = len(nums) - 1
            while l < r:
                sumOf = nums[i] + nums[l] + nums[r]
                if sumOf < 0:
                    l = l+1
                elif sumOf > 0:
                    r = r-1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1

        return result

        # result = []
        # for i in range(len(nums)):
        #     curr = -1 * nums[i]
        #     seen = {}
        #     for j in range(len(nums)):
        #         if j == i:
        #             continue
        #         complement = curr - nums[j]
        #         if complement in seen:
        #             foundSet = sorted([nums[i],nums[j],complement])
        #             if foundSet not in result:
        #                 result.append(foundSet)
        #         seen[nums[j]] = j
        # return result
